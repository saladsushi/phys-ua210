import astropy.io.fits
import matplotlib.pyplot as plt

hdu_list = astropy.io.fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

wavelength = 10**logwave

plt.figure(figsize=(14, 7))
for i in range(5):
    plt.plot(wavelength, flux[i], label=f'Galaxy {i+1}')

plt.xlabel('Wavelength (A)')
plt.ylabel('Flux (10^-17 erg/s/cm^2/A)')
plt.title('Spectra of Different Galaxies')
plt.legend()
plt.grid(True)
plt.show()
