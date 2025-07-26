import torch
from torch import optim

t_celsius = torch.tensor([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
t_unknown = torch.tensor([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])
t_unknown_normalize = t_unknown * 0.1

weight = torch.ones(())
bias = torch.zeros(())


def model(t_un, w, b):
    return t_un * w + b


def loss_fn(t_c, t_p):
    squared_diffs = (t_p - t_c) ** 2
    return squared_diffs.mean()


def dloss_fn(t_p, t_c):
    dsq_diffs = 2 * (t_p - t_c) / t_p.size(0)  # <1>
    return dsq_diffs


def dmodel_dw(t_u, w, b):
    return t_u


def dmodel_db(t_u, w, b):
    return 1.0


def grad_fn(t_u, t_c, t_p, w, b):
    dloss_dtp = dloss_fn(t_p, t_c)
    dloss_dw = dloss_dtp * dmodel_dw(t_u, w, b)
    dloss_db = dloss_dtp * dmodel_db(t_u, w, b)
    return torch.stack([dloss_dw.sum(), dloss_db.sum()])


# def training_loop(n_epochs, learning_rate, params, t_u, t_c):
# def training_loop(n_epochs, optimizer, params, t_u, t_c):
def training_loop(n_epochs, optimizer, params, train_t_u, val_t_u,
                      train_t_c, val_t_c):
    for epoch in range(1, n_epochs + 1):

        # if params.grad is not None:
        #     params.grad.zero_()

        train_t_p = model(train_t_u, *params)
        train_loss = loss_fn(train_t_p, train_t_c)

        val_t_p = model(val_t_u, *params)
        val_loss = loss_fn(val_t_p, val_t_c)

        # t_p = model(t_u, *params)
        # loss = loss_fn(t_p, t_c)
        # grad = grad_fn(t_u, t_c, t_p, *params)
        # loss.backward()

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        # with torch.no_grad():
        #     params -= learning_rate * params.grad

        # params = params - learning_rate * grad
        # if epoch % 500 == 0:
        #     print('Epoch %d, Loss %f' % (epoch, float(loss)))

        if epoch <= 3 or epoch % 500 == 0:
            print(f"Epoch {epoch}, Training loss {train_loss.item():.4f},"
                  f" Validation loss {val_loss.item():.4f}")

    return params


n_samples = t_unknown.shape[0]
n_val = int(0.2 * n_samples)

shuffled_indices = torch.randperm(n_samples)

train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]

train_t_u = t_unknown[train_indices]
train_t_c = t_celsius[train_indices]

val_t_u = t_unknown[val_indices]
val_t_c = t_celsius[val_indices]

train_t_un = 0.1 * train_t_u
val_t_un = 0.1 * val_t_u

learning_rate = 1e-2
params = torch.tensor([1.0, 0.0], requires_grad=True)
res = training_loop(
    n_epochs=3000,
    # learning_rate=1e-2,
    optimizer=optim.SGD([params], lr=learning_rate),
    # optimizer=optim.Adam([params], lr=learning_rate),
    params=params,
    # params=torch.tensor([1.0, 0.0]),
    train_t_u=train_t_un,
    val_t_u=val_t_un,
    train_t_c=train_t_c,
    val_t_c=val_t_c)
print(res)
