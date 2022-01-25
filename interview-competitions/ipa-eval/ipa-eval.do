*rmdir "export"

* establecer cd

mkdir "output"



use hh_round1.dta, clear

gen hhid1 = substr(hhid, 4, .)

order hhid1 head_gender head_education  size, first

destring read write hhid1, replace

replace head_gender = 0 if head_gender == 2

replace head_gender = 0 if hhid1 == 15064
replace head_education = 0 if hhid1 == 29038
replace read = 3 if hhid1 == 53024

drop hhid1

label variable hhid "Household ID"

save "export/hh_round_clean.dta", replace

import excel round2.xlsx, firstrow cellrange(B3:AB1602) sheet("round2") clear

bysort hhid: egen flag=count(hhid)
drop if flag == 1 | flag == 0

preserve

drop flag
export excel "export/dup.xlsx", sheet("duplicates", replace) firstrow(variables)

restore
keep hhid flag
export excel "export/dup.xlsx", sheet("num_dup", replace) firstrow(variables)

use hh_nr_round1.dta, clear
split crop_l, p()
drop crop_l

sort hhid

reshape long crop_l, i(crop_l* hhid)


rename crop_l con
sort hhid con


drop crop_l* _j

destring con, replace

gen crop_l = 1

replace crop_l = 0 if con == .

drop if con == . | co == -111

reshape wide crop_l, i(hhid) j(con)

forvalues i = 1/7 {
    replace crop_l`i' = 0 if crop_l`i' == .
}


sort hhid

save "export/hh_nr_round1_cl.dta", replace

use hh_round1, clear

append using "export/hh_nr_round1_cl.dta"

gsort -village

save "export/merge.dta", replace
