import numpy as np
from numba import njit, prange

@njit(cache=True, fastmath=True, parallel=True)
def matmul_turbo(A, B):
    """Turbo-charged Matrix Multiplication for Paradma"""
    if A.ndim == 2 and B.ndim == 1:
        # Matrix-Vector (common for similarity search)
        M, K = A.shape
        K2 = B.shape[0]
        assert K == K2
        C = np.zeros(M, dtype=A.dtype)
        for i in prange(M):
            val = 0.0
            for k in range(K):
                val += A[i, k] * B[k]
            C[i] = val
        return C
    elif A.ndim == 2 and B.ndim == 2:
        M, K = A.shape
        K2, N = B.shape
        assert K == K2
        C = np.zeros((M, N), dtype=A.dtype)
        for i in prange(M):
            for k in range(K):
                a_ik = A[i, k]
                for j in range(N):
                    C[i, j] += a_ik * B[k, j]
        return C
    return A @ B # Fallback

@njit(cache=True, fastmath=True, parallel=True)
def cosine_similarity_turbo(vectors, query):
    """Batch Cosine Similarity for Parag RAG"""
    M, K = vectors.shape
    K2 = query.shape[0]
    assert K == K2
    
    # Pre-calculate query norm
    query_norm = 0.0
    for i in range(K):
        query_norm += query[i] * query[i]
    query_norm = np.sqrt(query_norm)
    
    results = np.zeros(M, dtype=vectors.dtype)
    
    for i in prange(M):
        dot = 0.0
        vec_norm = 0.0
        for k in range(K):
            val = vectors[i, k]
            dot += val * query[k]
            vec_norm += val * val
        
        vec_norm = np.sqrt(vec_norm)
        if vec_norm > 0 and query_norm > 0:
            results[i] = dot / (vec_norm * query_norm)
        else:
            results[i] = 0.0
            
    return results

@njit(cache=True, fastmath=True, parallel=True)
def dot_turbo(a, b):
    """High-speed dot product"""
    return np.dot(a, b)

@njit(cache=True, fastmath=True, parallel=True)
def euclidean_distance_turbo(vectors, query):
    """Batch Euclidean Distance for Paradma"""
    M, K = vectors.shape
    results = np.zeros(M, dtype=vectors.dtype)
    for i in prange(M):
        dist = 0.0
        for k in range(K):
            diff = vectors[i, k] - query[k]
            dist += diff * diff
        results[i] = np.sqrt(dist)
    return results
