# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:25:27 2021

@author: jqj
"""
import math
import numpy as np
import time

res = 0
import time
import numpy as np
import math


def U1(H,a,p,c,q,FS,Kh,Kv,fh,fv,t,vs,vp,Xl,Xr,B,n):

    a=math.radians(a)
    q=math.radians(q)
    k1=math.tan(a)
    k2=math.tan(q)
    b1=(Xr-Xl)/n-0.1
    db=(2*((Xr-Xl)-n*b1))/(n*(n-1))
    b=np.zeros(n)
    for i in range(n):
        b[i]=b1+(i-1)*db
    # print(b)
    x=np.zeros(n+1)
    x[0]=0
    for i in range(n):
        x[i+1]=((i+1)*(b[0]+b[i]))/2
    O=(math.degrees(math.atan((H/(Xr-Xl))))-B)/n
    # print(O)
    h=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]==0:
            h[i]=0
        elif x[i]>0 and x[i]<=H/k1:
            h[i]=x[i]*(k1-math.tan(math.radians((i)*O+B)))
        else:
            h[i]=H-(x[i]*math.tan(math.radians((i)*O+B)))
            if h[i]<0:
                h[i]=0
    # print(x)
    # print(h)
    Q = np.zeros(n)
    for i in range(n):
        if x[i] <= H / k1 and x[i + 1] <= H / k1:
            Q[i] = math.atan((h[i] - h[i + 1] + b[i] * k1) / b[i])
        elif x[i] >= H / k1 and x[i + 1] >= H / k1:
            Q[i] = math.atan((h[i] - h[i + 1]) / b[i])
        else:
            Q[i] = math.atan((h[i] - h[i + 1] + H - x[i] * k1) / b[i])
    # for i in range(n):
    #     Q[i]=math.degrees(Q[i])
    # print(Q)
    hh=np.zeros(len(x)-1)
    for j in range(len(x)-1):
        hh[j]=(h[j]+h[j+1])/2
    # print(hh)
    S=np.zeros(n)
    C=np.zeros(n)
    L = np.zeros(n)
    W = np.zeros(n)
    Fh = np.zeros(n)
    Fv = np.zeros(n)
    for i in range(n):
        S[i]=math.sin(Q[i])
        C[i]=math.cos(Q[i])
        L[i] = b[i] / C[i]
        W[i] = p * b[i] * hh[i]
        Fh[i] = Kh*W[i]
        Fv[i] = Kv * W[i]
    # print(S)
    # print(C)
    # print(L)
    # print(W)
    # print(Fh)
    # print(Fv)
    m=np.zeros(n)
    for i in range(n-1):
        m[n-1]=math.cos(0-Q[n-1])-k2*math.sin(0-Q[n-1])
        m[i]=math.cos(Q[i+1]-Q[i])-k2*math.sin(Q[i+1]-Q[i])
    # print(m)


    P = np.zeros(n)
    # print(P)
    P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
    if P[0] < 0:
        P[0] = 0
    # print(P)
    for i in range(1,n):
        P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
    # print(P)
    P1 = np.zeros(n)
    P1 = P[0:n-1]
    # print(P1)
    arr = np.array(P1)

    if ((arr < 0).any()) == 3:
        g=np.argwhere(P1<0)
        g1 = g[0]
        g2 = g1[0]
        # print(g2)
        P[g2] = 0
        for i in range(g2+1,n):
            P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
    # print(P)

    Fs=0


    if abs(P[n - 1]) <= 3:
        Fs = FS
    else:
        while P[n-1] > 3:
            FS = FS - 0.001
            P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
            if P[0] < 0:
                P[0] = 0
            # print(P)
            for i in range(1,n):
                P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]

            # print(P)
            P1 = np.zeros(n)
            P1 = P[0:n - 1]
            # print(P1)
            arr = np.array(P1)
            if ((arr < 0).any()) == 1:
                g = np.argwhere(P1 < 0)
                g1 = g[0]
                g2 = g1[0]
                # print(g2)
                P[g2] = 0
                for i in range(g2 + 1, n):
                    P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]

        while P[n-1] < -3:
            FS = FS + 0.001
            P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
            if P[0] < 0:
                P[0] = 0
            # print(P)
            for i in range(1,n):
                P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]

            # print(P)
            P1 = np.zeros(n)
            P1 = P[0:n - 1]
            # print(P1)
            arr = np.array(P1)
            if ((arr < 0).any()) == 1:
                g = np.argwhere(P1 < 0)
                g1 = g[0]
                g2 = g1[0]
                # print(g2)
                P[g2] = 0


                for i in range(g2+1,n):
                    P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
            # print(P)



    Fs = FS
    print(P)
    print(Fs)
    # print(W)
    print(Fh)
    # print(L)
    # print(Q)
    # print(m)
    return Fs
def BSDtMIN(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, N):
    global res
    T = np.arange(0, t, 0.1)
    fs = np.zeros(len(T))
    for i in range(1, len(T)):
        fs[i] = BSD(H, a, p, c, q, Kh, Kv, fh, fv, T[i], FS, vs, vp, N)

    Min = fs[1]
    for i in range(len(T)):
        if Min >= fs[i] > 0:
            Min = 20 * fs[i]
    print(Min)
    res = Min
def BSD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, N):

    a = math.radians(a)
    q = math.radians(q)
    Xl = 0
    Xr = np.linspace(H / (math.tan(a)), H / (math.tan(a)) + H, N)
    Xo = np.linspace(-H, H, N)
    fs = math.inf * np.ones((len(Xr), len(Xo)))

    for i in (range(1, len(Xr))):
        for j in (range(1, len(Xo))):
            fs[i, j] = BISHOPD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, Xl, Xr[i], Xo[j], N);
            if H > -(Xr[i] - Xl) / H * (Xo[j] - (Xr[i] + Xl) / 2) + H / 2:
                fs[i, j] = 10
    min = fs[0][0]
    for i in range(len(Xr)):
        for j in range(len(Xo)):
            if (min >= fs[i][j] > 0):
                min = fs[i][j]
    return min
def BISHOPD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, Xl, Xr, Xo, N):
    k1 = math.tan(a)
    k2 = math.tan(q)
    Yo = -(Xr - Xl) / H * (Xo - (Xr + Xl) / 2) + H / 2
    R = ((Xo - Xl) ** 2 + Yo ** 2) ** 0.5
    x = np.linspace(Xl, Xr, N)
    S = (x - Xo) / R
    C = ((R ** 2 - (x - Xo) ** 2) ** 0.5) / R
    b = (Xr - Xl) / len(x)
    L = b / C
    h = np.zeros(len(x))
    for i in (range(1, len(x))):
        if x[i] <= 0:
            h[i] = (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo
        elif x[i] > 0 and x[i] <= H / k1:
            h[i] = k1 * x[i] + (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo
        else:
            h[i] = H + (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo

    if min(np.sign(h)) < 0:
        M1 = 10
        M2 = 1
    elif Xo > H / math.tan(2 * (math.atan(H / (Xr - Xl)))):
        M1 = 10
        M2 = 1
    else:
        FS = 1.1 * FS
        W = p * b * h
        Fh = Kh * p * b * vs * ((np.cos(2 * (math.pi) * fh * (t - (H - h) / (vs + 1e-10)))) - np.cos(
            2 * math.pi * fh * ((t - H / (vs + 1e-10))))) / (2 * math.pi * (fh + 1e-10))
        Fv = Kv * p * b * vp * ((np.cos(2 * (math.pi) * fv * (t - (H - h) / (vp + 1e-10)))) - np.cos(
            2 * math.pi * fv * ((t - H / (vp + 1e-10))))) / (2 * math.pi * (fv + 1e-10))
        M = c + (S * k2) / FS
        M1 = sum((c * L + (W - Fv) * k2) / M)
        M2 = (sum(W * S) + (sum(Fh * ((R ** 2 - (x - Xo) ** 2) ** 0.5) - (h / 2))) / R - sum(Fv * S))
        if M2.all() < 0:
            M2 = M1 / 10
        Fs = M1 / M2

        while abs(Fs - FS) >= 0.001:
            FS = Fs
            W = p * b * h
            Fh = Kh * p * b * vs * ((np.cos(2 * (math.pi) * fh * (t - (H - h) / (vs + 1e-10)))) - np.cos(
                2 * math.pi * fh * ((t - H / (vs + 1e-10))))) / (2 * math.pi * (fh + 1e-10))
            Fv = Kv * p * b * vp * ((np.cos(2 * (math.pi) * fv * (t - (H - h) / (vp + 1e-10)))) - np.cos(
                2 * math.pi * fv * ((t - H / (vp + 1e-10))))) / (2 * math.pi * (fv + 1e-10))
            M = c + (S * k2) / FS
            M1 = sum((c * L + (W - Fv) * k2) / M)
            M2 = (sum(W * S) + (sum(Fh * ((R ** 2 - (x - Xo) ** 2) ** 0.5) - (h / 2))) / R - sum(Fv * S))
            if M2.all() < 0:
                M2 = M1 / 10
            Fs = M1 / M2

        return Fs
def Ub(bi, ci, ψi, cii, ψii, Wi, Ui, ai, δi, PW, di, H, Kh, Kv, fh, fv, t, vs, vp, p, h, n):
    global res
    ψii = ψii + [0]
    δi = δi + [0]
    pi = [None] * n
    ei = [None] * n
    Ri = [None] * n
    Si = [None] * n
    Ai = [None] * n
    E = [None] * n
    Fh = [None] * n
    Fv = [None] * n

    # 宽度bi、底面粘聚力ci、摩擦角ψi、侧面粘聚力cii\
    # 侧面摩擦角ψii、滑块重度Wi、底滑面孔隙水压力Ui、底面与水平面夹角ai、侧面与竖直面的夹角δi、
    # PW，左侧面宽度di、坡高H
    for i in range(n):
        ψi[i] = math.radians(ψi[i])
        ψii[i] = math.radians(ψii[i])
        ai[i] = math.radians(ai[i])
        δi[i] = math.radians(δi[i])

    for i in range(n):
        Fh[i] = Kh[i] * p[i] * bi[i] * vs[i] / (2 * math.pi * (fh[i] + 1e-10)) * (
                    (np.cos(2 * (math.pi) * fh[i] * (t - (H[i] - h[i]) / (vs[i] + 1e-10)))) - np.cos(
                2 * math.pi * fh[i] * ((t - H[i] / (vs[i] + 1e-10)))))
        Fv[i] = Kv[i] * p[i] * bi[i] * vp[i] / (2 * math.pi * (fv[i] + 1e-10)) * (
                    (np.cos(2 * (math.pi) * fv[i] * (t - (H[i] - h[i]) / (vp[i] + 1e-10)))) - np.cos(
                2 * math.pi * fv[i] * ((t - H[i] / (vp[i] + 1e-10)))))
        pi[i] = Wi[i] * np.cos(ψi[i] - ai[i]) * np.cos(ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
        ei[i] = np.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * np.cos(ψii[i + 1]) / (
                    np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * np.cos(ψii[i]))
        Ri[i] = ci[i] * bi[i] / np.cos(ai[i]) - Ui[i] * np.tan(ψi[i])
        Si[i] = cii[i] * di[i] / np.cos(ai[i]) - PW[i] * np.tan(ψi[i])
        Si = Si + [0]

    for i in range(n):
        Ai[i] = ((Wi[i] - Fh[i]) * np.sin(ψi[i] - ai[i]) + Ri[i] * np.cos(ψi[i]) + Si[i + 1] * np.sin(
            ψi[i] - ai[i] - δi[i + 1]) - Si[i] * np.sin(ψi[i] - ai[i] - δi[i]) - Fv[i]) * np.cos(ψii[i]) / np.cos(
            ψi[i] - ai[i] + ψii[i] - δi[i + 1])

    ei.reverse()
    Ai.reverse()
    pi.reverse()
    Ei = [None] * n
    for i in range(n):
        Ei[i] = [1] + ei[0:i]

    from functools import reduce
    r = [None] * n
    for i in range(n):
        r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘

    sh = [a * b for a, b in zip(Ai, r)]
    xi = [a * b for a, b in zip(pi, r)]
    SH = 0
    XI = 0

    for i in range(0, len(sh)):
        SH = SH + sh[i]
    for i in range(0, len(xi)):
        XI = XI + xi[i]

    Ub = SH / XI

    Fs = 1
    if Ub < 0:

        while Ub < 0:

            Fs = Fs - 0.001

            # print(Fs)
            res = Fs
            ci = [i / Fs for i in ci]
            cii = [i / Fs for i in cii]
            pi = [None] * n
            ei = [None] * n
            Ri = [None] * n
            Si = [None] * n
            Ai = [None] * n
            E = [None] * n
            f1 = [None] * n
            f2 = [None] * n
            for i in range(n):
                f1[i] = np.tan(ψi[i]) / Fs
                f2[i] = np.tan(ψii[i]) / Fs
                ψi[i] = math.atan(f1[i])
                ψii[i] = math.atan(f2[i])

            for i in range(n):
                Fh[i] = Kh[i] * p[i] * bi[i] * vs[i] / (2 * math.pi * (fh[i] + 1e-10)) * (
                            (np.cos(2 * (math.pi) * fh[i] * (t - (H[i] - h[i]) / (vs[i] + 1e-10)))) - np.cos(
                        2 * math.pi * fh[i] * ((t - H[i] / (vs[i] + 1e-10)))))
                Fv[i] = Kv[i] * p[i] * bi[i] * vp[i] / (2 * math.pi * (fv[i] + 1e-10)) * (
                            (np.cos(2 * (math.pi) * fv[i] * (t - (H[i] - h[i]) / (vp[i] + 1e-10)))) - np.cos(
                        2 * math.pi * fv[i] * ((t - H[i] / (vp[i] + 1e-10)))))
                pi[i] = Wi[i] * np.cos(ψi[i] - ai[i]) * np.cos(ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
                ei[i] = np.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * np.cos(ψii[i + 1]) / (
                            np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * np.cos(ψii[i]))
                Ri[i] = ci[i] * bi[i] / np.cos(ai[i]) - Ui[i] * np.tan(ψi[i])
                Si[i] = cii[i] * di[i] / np.cos(ai[i]) - PW[i] * np.tan(ψi[i])
                Si = Si + [0]
            for i in range(n):
                Ai[i] = ((Wi[i] - Fh[i]) * np.sin(ψi[i] - ai[i]) + Ri[i] * np.cos(ψi[i]) + Si[i + 1] * np.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * np.sin(ψi[i] - ai[i] - δi[i]) - Fv[i]) * np.cos(
                    ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
            ei.reverse()
            Ai.reverse()
            pi.reverse()
            Ei = [None] * n
            for i in range(n):
                Ei[i] = [1] + ei[0:i]

            from functools import reduce
            r = [None] * n
            for i in range(n):
                r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘

            sh = [a * b for a, b in zip(Ai, r)]
            xi = [a * b for a, b in zip(pi, r)]
            SH = 0
            XI = 0

            for i in range(0, len(sh)):
                SH = SH + sh[i]
            for i in range(0, len(xi)):
                XI = XI + xi[i]
            Ub = SH / XI
            # print(Ub)

    else:
        while Ub > 0:

            Fs = Fs + 0.001

            # print(Fs)
            ci = [i / Fs for i in ci]
            cii = [i / Fs for i in cii]
            pi = [None] * n
            ei = [None] * n
            Ri = [None] * n
            Si = [None] * n
            Ai = [None] * n
            E = [None] * n
            f1 = [None] * n
            f2 = [None] * n
            for i in range(n):
                f1[i] = np.tan(ψi[i]) / Fs
                f2[i] = np.tan(ψii[i]) / Fs
                ψi[i] = math.atan(f1[i])
                ψii[i] = math.atan(f2[i])

            for i in range(n):
                Fh[i] = Kh[i] * p[i] * bi[i] * vs[i] / (2 * math.pi * (fh[i] + 1e-10)) * (
                            (np.cos(2 * (math.pi) * fh[i] * (t - (H[i] - h[i]) / (vs[i] + 1e-10)))) - np.cos(
                        2 * math.pi * fh[i] * ((t - H[i] / (vs[i] + 1e-10)))))
                Fv[i] = Kv[i] * p[i] * bi[i] * vp[i] / (2 * math.pi * (fv[i] + 1e-10)) * (
                            (np.cos(2 * (math.pi) * fv[i] * (t - (H[i] - h[i]) / (vp[i] + 1e-10)))) - np.cos(
                        2 * math.pi * fv[i] * ((t - H[i] / (vp[i] + 1e-10)))))
                pi[i] = Wi[i] * np.cos(ψi[i] - ai[i]) * np.cos(ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
                ei[i] = np.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * np.cos(ψii[i + 1]) / (
                            np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * np.cos(ψii[i]))
                Ri[i] = ci[i] * bi[i] / np.cos(ai[i]) - Ui[i] * np.tan(ψi[i])
                Si[i] = cii[i] * di[i] / np.cos(ai[i]) - PW[i] * np.tan(ψi[i])
                Si = Si + [0]
            for i in range(n):
                Ai[i] = ((Wi[i] - Fh[i]) * np.sin(ψi[i] - ai[i]) + Ri[i] * np.cos(ψi[i]) + Si[i + 1] * np.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * np.sin(ψi[i] - ai[i] - δi[i]) - Fv[i]) * np.cos(
                    ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
            ei.reverse()
            Ai.reverse()
            pi.reverse()
            Ei = [None] * n
            for i in range(n):
                Ei[i] = [1] + ei[0:i]

            from functools import reduce
            r = [None] * n
            for i in range(n):
                r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘

            sh = [a * b for a, b in zip(Ai, r)]
            xi = [a * b for a, b in zip(pi, r)]
            SH = 0
            XI = 0

            for i in range(0, len(sh)):
                SH = SH + sh[i]
            for i in range(0, len(xi)):
                XI = XI + xi[i]
            Ub = SH / XI

        return Ub
        # print(Ub)
mylist = []
def choosepic1():
    global mylist
    mylist = []
    path_ = askopenfilename()
    path.set(path_)
    img_RS = e1.get()
    with open(img_RS,'r') as f:
        data = f.readlines()
    data = [list(map(float,i.replace('\n','').split(','))) for i in data]
    for i in data:
        if len(i) == 1:
            mylist.append(i[0])
        else:
            mylist.append(i)
    l1.config(text = '当前文件：' + img_RS.split("/")[-1])
def choosepic3():
    aw = []
    for i in mylist:
        try:
            for j in i:
                if int(j) == j:
                    aw.append(int(j))
                else:
                    aw.append(j)
        except:
            if int(i) == i:
                aw.append(int(i))
            else:
                aw.append(i)
    print(aw)
    BSDtMIN(*aw)
    print(res)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
def choosepic2():
    for i in range(len(mylist)):
        try:
            mylist[i] = int(mylist[i])
        except:
            pass
    print(mylist)
    Ub(*mylist)
    print(res)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
def choosepic4():
    aw = []
    for i in mylist:
        try:
            for j in i:
                if int(j) == j:
                    aw.append(int(j))
                else:
                    aw.append(j)
        except:
            if int(i) == i:
                aw.append(int(i))
            else:
                aw.append(i)
    print(aw)
    res = U1(*aw)
    print(res)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
if __name__ == "__main__":
    import os
    import tkinter.messagebox
    import tkinter as tk

    from tkinter import *
    from tkinter.filedialog import askopenfilename
    root = Tk()
    root.title('UI')
    root.geometry('550x300')
    path = StringVar()
    Button(root, width=12, height=1, text='选择文件', command=choosepic1).place(x=30, y=250)
    Button(root, width=12, height=1, text='Sarma', command=choosepic2).place(x=130, y=250)
    Button(root, width=12, height=1, text='Bishop', command=choosepic3).place(x=230, y=250)
    Button(root, width=12, height=1, text='传递系数动力法', command=choosepic4).place(x=330, y=250)
    Button(root, width=12, height=1, text='传递系数静力法', command=choosepic4).place(x=430, y=250)
    e1 = Entry(root, state='readonly', text=path)
    l1 = Label(root,text='当前文件：无',font=(14))
    l1.place(x=130,y=110)
    l2 = Label(root,text='根据Excel或txt中的数据\n得到边坡原始参数',font=(14))
    l2.place(x=150,y=20)
    root.mainloop()