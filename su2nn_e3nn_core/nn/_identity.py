import torch

from su2nn_e3nn_core import su2 #!
from su2nn_e3nn_core.util.jit import compile_mode


@compile_mode('trace')
class Identity(torch.nn.Module):
    r'''Identity operation

    Parameters
    ----------
    irreps_in : `su2nn.su2.Irreps`

    irreps_out : `su2nn.su2.Irreps`
    '''

    def __init__(self, irreps_in, irreps_out):
        super().__init__()

        self.irreps_in = su2.Irreps(irreps_in).simplify()
        self.irreps_out = su2.Irreps(irreps_out).simplify()

        assert self.irreps_in == self.irreps_out

        output_mask = torch.cat([torch.ones(mul * (2 * l + 1)) for mul, (l, _p, _t) in self.irreps_out])
        self.register_buffer('output_mask', output_mask)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.irreps_in} -> {self.irreps_out})'

    def forward(
        # pylint: disable=no-self-use
        self,
        features,
    ):
        '''evaluate'''
        return features