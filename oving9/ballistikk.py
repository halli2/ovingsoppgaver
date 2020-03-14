import numpy as np
import matplotlib.pyplot as plt

# Grensesnitt: Evaluate
#   evaluate(tidspunkt, tilstandsvektor) -> endringsvektor

class Num_integrator:
    def __init__(self, lengde_steg, slutt_tid):
        self.lengde_steg = lengde_steg
        self.slutt_tid = slutt_tid
        antall_steg = slutt_tid / lengde_steg + 1
        self.antall_steg_int = round(antall_steg)
        idx_tidspunkt = []
        for x in range(self.antall_steg_int):
            idx_tidspunkt.append([x * lengde_steg, x])
        self.tids_matrise = np.array(idx_tidspunkt)


    def integrate(self, funksjonssobjekt, starttilstand):
        tilstandsvektor = starttilstand[:] # Måtte slice for å ikke bare få en fortsettelse!
        retur_matrise = np.array([tilstandsvektor])
        for _ in self.tids_matrise[1:, 0]:
            endringsvektor = funksjonssobjekt.evaluate(tilstandsvektor, self.lengde_steg)
            for idx, verdi in enumerate(endringsvektor):
                tilstandsvektor[idx] += self.lengde_steg * verdi
            retur_matrise = np.append(retur_matrise, [tilstandsvektor], axis=0)
           # np.append(x, [[1,2]], axis = 0)
           # np.r_[x,[[1,2]]]
        return retur_matrise


# NUmerisk integrator med iterator (frivillig)
class NumeriskIntegrator:
    def __init__(self, lengde_steg, slutt_tid, funksjonssobjekt, starttilstand):
        self.lengde_steg = lengde_steg
        self.slutt_tid = slutt_tid
        self.funksjonssobjekt = funksjonssobjekt
        self.tilstandsvektor = starttilstand[:]
        antall_steg = slutt_tid / lengde_steg 
        self.antall_steg_int = round(antall_steg)
        self.k = 0

    def __iter__(self):
        return IntegratorIterator(self)


class IntegratorIterator:
    def __init__(self, integrator):
        self.integrator = integrator
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.k >= self.integrator.antall_steg_int:
            raise StopIteration
        endringsvektor = self.integrator.funksjonssobjekt.evaluate(self.integrator.tilstandsvektor, self.integrator.lengde_steg)
        self.k += 1
        for idx, verdi in enumerate(endringsvektor):
            self.integrator.tilstandsvektor[idx] += self.integrator.lengde_steg * verdi
        return self.integrator.tilstandsvektor



# Tar inn en starttilstand-vektor [x_start, y_start, x_fart, y_fart] og tyngdekraft (standard -9.81m/s)
class Basis_kulebane:
    def __init__(self, tyngdekraft=-9.81):
        self.tyngdekraft = tyngdekraft

    def evaluate(self, tilstandsvektor, tidspunkt):
        endringsvektor = [tilstandsvektor[2], tilstandsvektor[3], 0, self.tyngdekraft]
        return endringsvektor

class Kulebane_med_luftmotstand:
    def __init__(self, luftmostand=0, tyngdekraft=-9.91):
        self.luftmostand = luftmostand
        self.tyngdekraft = tyngdekraft
    
    # Er dette rett?
    def evaluate(self, tilstandsvektor, tidspunkt):
        x_fart = tilstandsvektor[2]
        y_fart = tilstandsvektor[3]
        fart = np.sqrt(x_fart**2 + y_fart**2)
        x_aks = - (self.luftmostand * x_fart * fart)
        y_aks = self.tyngdekraft - (self.luftmostand * y_fart * fart)
        endringsvektor = [x_fart, y_fart, x_aks, y_aks]
        return endringsvektor


if __name__ == "__main__":
    tidssteg = 0.01
    luftmotstand = 0.5
    starttilstand = [0, 0, 1, 2]
    slutt_tid = 0.45

    basis_bane = Basis_kulebane()
    bane = Kulebane_med_luftmotstand(luftmotstand)

    integrator_basis = NumeriskIntegrator(tidssteg, slutt_tid, basis_bane, starttilstand)
    integrator_luftmotstand = NumeriskIntegrator(tidssteg, slutt_tid, bane, starttilstand)

    # Itererer
    tilstand_basis = np.array([starttilstand])
    for tilstand in integrator_basis:
        tilstand_basis = np.append(tilstand_basis, [tilstand], axis=0)
    tilstand_luft = np.array([starttilstand])
    for tilstand in integrator_luftmotstand:
        tilstand_luft = np.append(tilstand_luft, [tilstand], axis=0)

    plt.plot(tilstand_basis[:, 0], tilstand_basis[:, 1], tilstand_luft[:, 0], tilstand_luft[:, 1])
    plt.grid()
    plt.show()

    #integrator = Num_integrator(tidssteg, slutt_tid)
    #tilstand_basis = integrator.integrate(basis_bane, starttilstand)
    #tilstand_luft = integrator.integrate(bane, starttilstand)
    #plt.plot(tilstand_basis[:,0], tilstand_basis[:, 1], tilstand_luft[:, 0], tilstand_luft[:, 1])
    #plt.plot(tilstand_luft[:, 0], tilstand_luft[:, 1])