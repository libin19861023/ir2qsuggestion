from collections import Counter

import math

from features.feature import Feature


class CosineSimilarity(Feature):
    @staticmethod
    def calculate_feature(compared_query, queries):
        features = []

        cq_vector = CosineSimilarity.query2vector(compared_query)
        cq_vector_count = Counter(cq_vector)
        cq_vector_set = set(cq_vector)
        l_cq = CosineSimilarity.vector_len(cq_vector_count)
        for q in queries:
            q_vector = CosineSimilarity.query2vector(q)
            indexes = cq_vector_set.union(set(q_vector))
            c = Counter(q_vector)
            dot = 0
            for i in indexes:
                dot += cq_vector_count[i] * c[i]

            l_q = CosineSimilarity.vector_len(c)
            try:
                features.append(dot/(l_cq*l_q))
            except:
                features.append(0)
            # I don't think this makes sence as the queries in this method are not necessarily the coocurence queries
            # Feature.cooccurrences[compared_query]['cosinesimilarity'] = features
        return features

    @staticmethod
    def query2vector(query):
        return map(lambda x: CosineSimilarity.w2n[x], query.split())

    @staticmethod
    def vector_len(vector_counter):
        return math.sqrt(sum(map(lambda x: x**2, vector_counter.values())))

