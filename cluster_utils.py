import torch

# centroids can be found as Z = Y_inv * X
def centroids(X, Y):
    return torch.mm(inverse(Y), X)
    
def energy(dist, X, Y, Z):
    return dist.phi(X).sum() - \
           dist.phi(torch.mm(Y, Z)).sum() - \
           torch.trace(torch.mm(X - torch.mm(Y, Z), dist.grad_phi(torch.mm(Y, Z)).t()))
    
def inverse(X):
    u, s, v = torch.svd(X)
    h = torch.max(s) * float(max(X.size(0),X.size(1))) * 1e-15
    indices = torch.ge(s,h)
    indices2 = indices.eq(0)
    s[indices] = 1.0 / s[indices]
    s[indices2] = 0
    return torch.mm(torch.mm(v, torch.diag(s)), u.t())


if __name__ == '__main__':
	Y_init = torch.eye(n_cluster).index(torch.floor(torch.rand(X.size(0)) * n_cluster).long())
	Y = Y_init
	# Y = update_H(Y, u_r)
	# plot(u_r, Y)
	Y = solve_H(Y_init, u_r,Y=None, iters=100)
	# plot(u_r, Y)
	Y_inv = inv_H(Y)
	Y_inv.sum(1)