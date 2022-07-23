import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default="Cora", help="Cora, CiteSeer, PubMed, Computers, Photo")

    # masking
    parser.add_argument("--repetitions", type=int, default=2)
    parser.add_argument('--imb_ratio', type=float, default=10,help='Imbalance Ratio')
    # Encoder
    parser.add_argument("--layers", nargs='+', default='[128,128]', help="The number of units of each layer of the GNN. Default is [256]")
    parser.add_argument('--n_head', type=int, default=8,help='the number of heads in GAT')


    # optimization
    parser.add_argument("--epochs", '-e', type=int, default=2000, help="The number of epochs")
    parser.add_argument("--lr", '-lr', type=float, default=0.005, help="Learning rate. Default is 0.0001.")
    parser.add_argument("--decay", type=float, default=5e-4, help="Learning rate. Default is 0.0001.")
    parser.add_argument("--patience", type=int, default=300)


    parser.add_argument("--rounds", type=int, default=40)
    parser.add_argument("--clustering", action='store_true', default=True)
    parser.add_argument("--num_K", type=int, default=200)
    parser.add_argument("--device", '-d', type=int, default=0, help="GPU to use")

    return parser.parse_known_args()[0]
