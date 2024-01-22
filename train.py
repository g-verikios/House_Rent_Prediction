# %%
#@ IMPORTS



# PARAMETERS (normally given through CLI for eg.)

control_var = {           # number of estimators

}
output_file = 'model.bin'

# %% 
# DATA PREPARATION
data = pd.read_csv('')


# %% 
# SAVE THE MODEL

with open(output_file, 'wb') as f_out:

    pickle.dump(model, f_out)

print(f'the model is saved to {output_file}')
