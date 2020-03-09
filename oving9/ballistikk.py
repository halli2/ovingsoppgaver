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
        tilstandsvektor = starttilstand
        retur_matrise = np.array([tilstandsvektor])
        for tid in self.tids_matrise[1:, 0]:
            endringsvektor = funksjonssobjekt.evaluate(tilstandsvektor, self.lengde_steg)
            for idx, verdi in enumerate(endringsvektor):
                tilstandsvektor[idx] += self.lengde_steg * verdi
            retur_matrise = np.append(retur_matrise, [tilstandsvektor], axis=0)
           # np.append(x, [[1,2]], axis = 0)
           # np.r_[x,[[1,2]]]
        return retur_matrise



        



# Tar inn en starttilstand-vektor [x_start, y_start, x_fart, y_fart] og tyngdekraft (standard -9.81m/s)
class Basis_kulebane:
    def __init__(self, tyngdekraft=-9.81):
        self.tyngdekraft = tyngdekraft

    # x_fart kan endrer seg ikke (ingen luftmostand)
    def evaluate(self, tilstandsvektor, tidspunkt):
        y_fart = tilstandsvektor[3] + (self.tyngdekraft * tidspunkt)
        endringsvektor = [tilstandsvektor[2], y_fart, 0, self.tyngdekraft]
        return endringsvektor

class Kulebane_med_luftmotstand:
    def __init__(self, luftmostand=0, tyngdekraft=-9.91):
        self.luftmostand = luftmostand
        self.tyngdekraft = tyngdekraft
    
    def evaluate(self, tilstandsvektor, tidspunkt):
        # Fatter ikke helt utregningen til akselerasjon med luftmotstand. 
        # SPØR PÅ ØVINGSTIME
        print(endringsvektor)
        return endringsvektor


if __name__ == "__main__":
    tidssteg = 0.01
    luftmotstand = 0.5
    starttilstand = [0, 0, 5, 10]
    slutt_tid = 2
    #basis_bane = Basis_kulebane()
    bane = Kulebane_med_luftmotstand(luftmotstand)

    integrator = Num_integrator(tidssteg, slutt_tid)
    #xy_basis = integrator.integrate(basis_bane, starttilstand)
    xy_luft = integrator.integrate(bane, starttilstand)

    #plt.plot(xy_basis[:,0], xy_basis[:, 1])
    plt.plot(xy_luft[:, 0], xy_luft[:, 1])
    plt.show()