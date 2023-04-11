

import statsmodels.api as sm
import pandas as pd

def fit_nb_model(df, outcome):

    # Create outcome and predictor variables
    y = df[outcome].reset_index(drop=True)
    # select variables from tmax to wday 7
    X = df.loc[:, 'tmax':'wday'].reset_index(drop=True)
    X = sm.add_constant(X)

    # Fit negative binomial regression model
    nb_model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
    nb_results = nb_model.fit()

    return nb_results


def prepare_model_data(df):

    mod_df = (df.loc[:, ['violent_offense_count', 'misdemeanor_count', 'felony_count',
                  'tmax', 'tmin', 'year', 'dispatch_quarter', 'dispatch_wday']]
              .rename(columns={'violent_offense_count': 'vo',
                              'misdemeanor_count': 'mis',
                              'felony_count': 'fel',
                              'dispatch_quarter': 'q',
                              'dispatch_wday': 'wday'})
              # tmax and tmin will be interpreted on a 10-unit increase
              .assign(tmax=lambda x: x.tmax/10, tmin=lambda x: x.tmin/10)
              # factorize wday variable
              .assign(wday=lambda x: pd.factorize(x.wday)[0])
              .drop(columns=['q']))

    return mod_df