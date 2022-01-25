#!/usr/bin/env python
# coding: utf-8

# ## Credit Risk
# *Víctor Acevedo*

# In[1]:


from scipy.stats import norm


# In[2]:


expectedLoss = 0.6
sd = 2
maxLossTolerable = norm(loc = expectedLoss, scale = sd).ppf(0.999)


# In[3]:


maxLossTolerable


# In[3]:


actualEconomicCapital = 5


# In[4]:


ecoCapitalRequired = maxLossTolerable - expectedLoss
additionalEconomic = ecoCapitalRequired - actualEconomicCapital
additionalEconomic

