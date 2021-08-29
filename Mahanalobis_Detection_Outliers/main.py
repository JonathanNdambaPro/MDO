import pandas as pd
import numpy as np
from scipy.spatial import distance

from sklearn.mixture import BayesianGaussianMixture, GaussianMixture
from sklearn.base import BaseEstimator, TransformerMixin

import typing as t


class Mdo(BaseEstimator, TransformerMixin):
    """
    On utilise la distance de Mahanalobis pour definir un score pour chaque point,
    plus le score est eleve plus le point est aberrant
    """

    def __init__(self) -> None:
        return self

    def Frequentist_gmm_inference(
        self, data: t.Union[pd.DataFrame, np.ndarray], **params
    ) -> None:
        """
        Frequentist inference of parameters by the EM algorithms,
        accept only DataFrame with numerical data, please do the feature engineering before enter the Dataframe
        :type data: Pd.DataFrame
        :return None:
        """
        gmm = GaussianMixture(**params)
        gmm.fit(data)

        self.means = gmm.means_
        self.precision = gmm.precisions_
        self.weight = gmm.weights_
        self.label = gmm.predict(data)
        self.nrb_comp = gmm.n_components

    def Bayesian_gmm_inference(
        self, data: t.Union[pd.DataFrame, np.ndarray], **params
    ) -> None:
        """
        Bayesian inference of parameters by the EM algorithms of sklearn,
        accept only DataFrame with numerical data, please do the feature engineering before enter the Dataframe
        :param data: Set of data to do the inference
        :return: None
        """
        Bayesian_gmm = BayesianGaussianMixture(**params)
        Bayesian_gmm.fit(data)

        self.means = Bayesian_gmm.means_
        self.precision = Bayesian_gmm.precisions_
        self.weight = Bayesian_gmm.weights_
        self.label = Bayesian_gmm.predict(data)
        self.nrb_comp = Bayesian_gmm.n_components

    def global_mahanalobis(self, data: t.Union[pd.DataFrame, np.ndarray]) -> t.List:
        """
        evaluate the weighted average distance from clusters
        :param data: data to check
        :return: None
        """
        self.mahanalobis_global = []
        for i in range(data.shape[0]):

            for means, precision, weight in zip(
                self.means, self.precision, self.weight
            ):
                dist_point = weight * distance.mahalanobis(means, data[i], precision)
            self.mahanalobis_global.append(dist_point)

        return self.mahanalobis_global

    def local_mahanalobis(self, data: t.Union[pd.DataFrame, np.ndarray]) -> t.List:
        """
        evaluate the distance of the nearest cluster (i.e  the cluster which the point belongs)
        :param data: data to check
        :return: None
        """
        self.mahanalobis_local = []

        for i in range(data.shape[0]):
            means = self.means[self.label[i]]
            precision = self.precision[self.label[i]]
            dist_point = distance.mahalanobis(means, data[i], precision)
            self.mahanalobis_local.append(dist_point)

        return self.mahanalobis_local

    def fit(self, data: t.Union[pd.DataFrame, np.ndarray], y=None):
        return self

    def transform(
        self,
        data: t.Union[pd.DataFrame, np.ndarray],
        inference_type: str = "bayesian",
        **params
    ) -> t.Union[None, pd.DataFrame]:
        """
        fitting of the distance
        :param data: data to check
        :param inference_type: types of inference (bayesian or frequentist)
        :param params: parameters for the inference
        :return: None
        """
        if inference_type == "bayesian":
            self.Bayesian_gmm_inference(data, **params)
        if inference_type == "frequentist":
            self.Frequentist_gmm_inference(data, **params)

        self.global_mahanalobis(data)
        self.local_mahanalobis(data)

        if isinstance(data, pd.DataFrame):
            data_with_distance = data.copy()
            data_with_distance["local_metrics"] = self.mahanalobis_local
            data_with_distance["global_metrics"] = self.mahanalobis_global

            return data_with_distance

        else:
            return None

    def get_scoring(self, scoring="global"):
        """
        Get the scoring define by the mahanalobis distance (local or global)
        :param scoring: define if the methods return local scoring or global
        :return:
        """
        if scoring == "local":
            return self.mahanalobis_local
        elif scoring == "global":
            return self.mahanalobis_global
