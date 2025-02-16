import numpy as np
import matplotlib

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def unscented_transform(X, Wm, Wc, noise_cov):
    mean = np.dot(Wm, X)
    cov = np.dot(Wc * (X - mean), (X - mean).T) + noise_cov
    return mean, cov

def UKF(x, P, Q, R, f, h, u, z):
    # Parameters
    n = len(x)
    alpha = 1e-3
    kappa = 0
    beta = 2
    lambda_ = alpha**2 * (n + kappa) - n

    # Weights
    Wm = np.full(2*n + 1, 1 / (2 * (n + lambda_)))
    Wm[0] = lambda_ / (n + lambda_)
    Wc = Wm.copy()
    Wc[0] += (1 - alpha**2 + beta)

    # Sigma points
    X = np.zeros((2*n + 1, n))
    X[0] = x
    sqrt_P = np.linalg.cholesky((n + lambda_) * P)
    for i in range(n):
        X[i + 1] = x + sqrt_P[i]
        X[n + i + 1] = x - sqrt_P[i]

    # Predict
    X = f(X, u)
    x_pred, P_pred = unscented_transform(X, Wm, Wc, Q)

    # Update
    Z = h(X)
    z_pred, P_zz = unscented_transform(Z, Wm, Wc, R)
    P_xz = np.dot(Wc * (X - x_pred), (Z - z_pred).T)

    K = np.dot(P_xz, np.linalg.inv(P_zz))
    x_est = x_pred + np.dot(K, (z - z_pred))
    P_est = P_pred - np.dot(K, np.dot(P_zz, K.T))

    return x_est, P_est

# Example usage
def f(X, u):
    return sigmoid(X) + u

def h(X):
    return X**2

x = np.array([0.5])  # Initial state
P = np.array([[0.1]])  # Initial covariance
Q = np.array([[0.01]])  # Process noise covariance
R = np.array([[0.1]])  # Measurement noise covariance
u = np.array([0.1])  # Input
z = np.array([0.7])  # Measurement

x_est, P_est = UKF(x, P, Q, R, f, h, u, z)

print("Estimated state:", x_est)
print("Estimated covariance:", P_est)