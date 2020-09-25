import argparse

import numpy
from matplotlib import dates as mdates
from matplotlib import pyplot

parser = argparse.ArgumentParser()
parser.add_argument("output", type=str)

args, _ = parser.parse_known_args()

FONTSIZE = 16
MARKERSIZE = 6

# Total, #1, #500
data = numpy.asarray([[1.12857000e+03, 5.97000000e+01, 4.20000000e-01],
                      [1.49335000e+03, 1.24000000e+02, 4.70000000e-01],
                      [2.31701000e+03, 1.43400000e+02, 8.40000000e-01],
                      [2.73224000e+03, 1.70000000e+02, 1.16000000e+00],
                      [3.92700000e+03, 1.70000000e+02, 1.96000000e+00],
                      [4.78434000e+03, 1.70000000e+02, 2.49000000e+00],
                      [5.89224000e+03, 2.20400000e+02, 3.31000000e+00],
                      [7.98124000e+03, 3.68200000e+02, 4.62000000e+00],
                      [1.28441900e+04, 1.06800000e+03, 7.67000000e+00],
                      [1.68981200e+04, 1.33800000e+03, 9.51000000e+00],
                      [2.26251400e+04, 1.33800000e+03, 1.33900000e+01],
                      [2.93676000e+04, 1.33800000e+03, 1.71200000e+01],
                      [3.90625700e+04, 2.12100000e+03, 2.47000000e+01],
                      [5.09385600e+04, 2.37900000e+03, 3.30900000e+01],
                      [6.42301100e+04, 2.37900000e+03, 4.38200000e+01],
                      [8.80824500e+04, 4.93800000e+03, 5.53000000e+01],
                      [1.08276780e+05, 7.22600000e+03, 6.77800000e+01],
                      [1.34977510e+05, 7.22600000e+03, 9.43000000e+01],
                      [2.22263770e+05, 3.58600000e+04, 1.34300000e+02],
                      [2.91814160e+05, 3.58600000e+04, 1.95800000e+02],
                      [3.70049260e+05, 3.58600000e+04, 2.41400000e+02],
                      [5.26740410e+05, 3.58600000e+04, 3.78600000e+02],
                      [8.12313210e+05, 3.58600000e+04, 6.06900000e+02],
                      [1.12883452e+06, 7.07200000e+04, 8.40020000e+02],
                      [1.69488664e+06, 1.36800000e+05, 1.16600000e+03],
                      [2.29934168e+06, 2.80600000e+05, 1.64570000e+03],
                      [2.78946547e+06, 2.80600000e+05, 2.02600000e+03],
                      [3.52786761e+06, 2.80600000e+05, 2.73690000e+03],
                      [4.95060048e+06, 2.80600000e+05, 4.03100000e+03],
                      [6.97759351e+06, 4.78200000e+05, 5.93733000e+03],
                      [1.21526911e+07, 1.02600000e+06, 8.99678000e+03],
                      [1.73735201e+07, 1.10500000e+06, 1.25935000e+04],
                      [2.26407896e+07, 1.10500000e+06, 1.71100000e+04],
                      [2.80064501e+07, 1.75900000e+06, 2.00700000e+04],
                      [3.24346846e+07, 1.75900000e+06, 2.46700000e+04],
                      [4.37868817e+07, 2.56600000e+06, 3.11243600e+04],
                      [5.89300258e+07, 8.16200000e+06, 4.01872900e+04],
                      [7.40696337e+07, 1.05100000e+07, 5.09414000e+04],
                      [1.23417787e+08, 1.63247510e+07, 6.08244000e+04],
                      [1.62139387e+08, 1.75900000e+07, 7.64110000e+04],
                      [2.28566576e+08, 3.38627000e+07, 9.66460000e+04],
                      [2.54971493e+08, 3.38627000e+07, 1.17992000e+05],
                      [2.78638938e+08, 3.38627000e+07, 1.34248880e+05],
                      [3.13022096e+08, 3.38627000e+07, 1.53357900e+05],
                      [3.64140347e+08, 3.38627000e+07, 1.64790720e+05],
                      [4.22609597e+08, 3.38627000e+07, 2.06400000e+05],
                      [5.72075796e+08, 9.30145939e+07, 2.86239700e+05],
                      [6.76771901e+08, 9.30145939e+07, 3.50400000e+05],
                      [7.53276959e+08, 9.30145939e+07, 4.33300000e+05],
                      [8.49580690e+08, 9.30145939e+07, 5.48672000e+05],
                      [1.21091486e+09, 1.22300000e+08, 7.15551000e+05],
                      [1.41495558e+09, 1.43500000e+08, 8.74800000e+05],
                      [1.55957538e+09, 1.48600000e+08, 1.02100000e+06],
                      [1.64688714e+09, 1.48600000e+08, 1.14200000e+06],
                      [2.20613439e+09, 4.15530000e+08, 1.22800000e+06]])

dates = numpy.asarray([numpy.datetime64(f'{Y}-{M:02d}-01', 'D')
                       for Y in range(1993, 2021)
                       for M in ([5, 10] if Y != 2020 else [5])])


fig = pyplot.figure(figsize=(9, 5), frameon=False)
ax = fig.add_subplot(111)

ax.plot(dates, data[:, 0], marker="o", label="Sum", markersize=MARKERSIZE)
ax.plot(dates, data[:, 1], marker="^", label="#1", markersize=MARKERSIZE)
ax.plot(dates, data[:, 2], marker="s", label="#500", markersize=MARKERSIZE)
years = mdates.YearLocator(2)
years_fmt = mdates.DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

ax.semilogy()

ax.set_xlabel("Date", fontsize=FONTSIZE)
ax.set_ylabel("Performance [GFlops/s]", fontsize=FONTSIZE)
ax.legend(fontsize=FONTSIZE)

fig.savefig(
    args.output,
    orientation="landscape",
    transparent=True,
    bbox_inches="tight",
)
