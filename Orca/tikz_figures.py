svp_rel_energies = []
tzvpd_rel_energies = []
dmf_rel_energies = []

class TikzPicture():
    def __init__(self):
        pass


    picture_settings = r"""[
                    xscale=0.9,
                    yscale=0.15,
                    svp_level/.style={draw=blue!100,very thick},
                    svp_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    svp_desc/.style={draw=none,font=\small, anchor=north, fill opacity=0},
                    svp_mol/.style={draw=none,font=\small, anchor=south, fill opacity=0},
                    tzvpd_level/.style={draw=red!100,very thick},
                    tzvpd_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    tzvpd_desc/.style={font=\small, anchor=north, fill opacity=0},          
                    tzvpd_mol/.style={draw=none,font=\small, anchor=south},
                    dmf_level/.style={draw=green!100,very thick},
                    dmf_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    dmf_desc/.style={font=\small, anchor=north, fill opacity=0},          
                    dmf_mol/.style={draw=none,font=\small, anchor=south, fill=none},
                    gibbs/.style={font=\footnotesize, below, text width=25mm, align=right, xshift=-5mm, }]"""

    def make_tikz_settings(self):
        picture_settings = r"""[
                        xscale=0.9,
                        yscale=0.15,
                        svp_level/.style={draw=blue!100,very thick},
                        svp_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                        svp_desc/.style={draw=none,font=\small, anchor=north, fill opacity=0},
                        svp_mol/.style={draw=none,font=\small, anchor=south, fill opacity=0},
                        tzvpd_level/.style={draw=red!100,very thick},
                        tzvpd_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                        tzvpd_desc/.style={font=\small, anchor=north, fill opacity=0},          
                        tzvpd_mol/.style={draw=none,font=\small, anchor=south},
                        dmf_level/.style={draw=green!100,very thick},
                        dmf_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                        dmf_desc/.style={font=\small, anchor=north, fill opacity=0},          
                        dmf_mol/.style={draw=none,font=\small, anchor=south, fill=none},
                        gibbs/.style={font=\footnotesize, below, text width=25mm, align=right, xshift=-5mm, }]"""
        return picture_settings

    def make_tikz_picture(self):
        tikz_str = ''
        tikz_str += f'\\begin{{tikzpicture}}[{self.make_tikz_settings}]'

        # Do everything else

        tikz_str += '\\end{tikzpicture}'



figure_template = r"""\begin{figure}[htb]
    \centering
    \begin{tikzpicture}[
                    xscale=0.9,
                    yscale=0.15,
                    svp_level/.style={draw=blue!100,very thick},
                    svp_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    svp_desc/.style={draw=none,font=\small, anchor=north, fill opacity=0},
                    svp_mol/.style={draw=none,font=\small, anchor=south, fill opacity=0},
                    tzvpd_level/.style={draw=red!100,very thick},
                    tzvpd_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    tzvpd_desc/.style={font=\small, anchor=north, fill opacity=0},          
                    tzvpd_mol/.style={draw=none,font=\small, anchor=south},
                    dmf_level/.style={draw=green!100,very thick},
                    dmf_reac/.style={->, shorten >=2pt,shorten <=2pt,>=stealth},
                    dmf_desc/.style={font=\small, anchor=north, fill opacity=0},          
                    dmf_mol/.style={draw=none,font=\small, anchor=south, fill=none},
                    gibbs/.style={font=\footnotesize, below, text width=25mm, align=right, xshift=-5mm, }]
    %%%%%% SVP
    \draw[dashed] (0,0) node[anchor=east] {$\Delta G$ = 0} -- (14,0);
    \draw[svp_level] (0,11.91) -- ++(1,0) 
    %node[svp_mol] {}%{\chemfig{Cl- + CH3Br}} 
    node[svp_desc] {$\Delta G$=11.91} 
    -- ++(1,0);
    
    \draw[svp_reac] (2, 11.91) -- (3, 0);
    
    \draw[svp_level] (3,0) -- ++(1,0) 
    node[svp_mol] {\ce{Cl- \bond{...} CH3Br}}
    node[svp_desc] {$\Delta G$=0}
    -- ++(1,0);
    
    \draw[svp_reac] (5,0) -- (6, 1.03); 
    
    \draw[svp_level] (6,1.03) -- ++(1,0) 
    node[gibbs, yshift=-3mm] {\colorbox{blue!15}{$\Delta G_{SVP}$=1.03}\\ \colorbox{red!15}{$\Delta G_{TZVPD}$=4.88}\\\colorbox{green!15}{$ \Delta G_{DMF}$=10.02}}
    node[svp_mol] {\ce{[Cl\bond{...}CH3 \bond{...}Br]-}} 
    node[svp_desc] {$\Delta G$=1.03} 
    -- ++(1,0);
    
    \draw[svp_reac] (8,1.03) -- (9, -9.98);
    
    \draw[svp_level] (9,-9.98) -- ++(1,0) 
    node[gibbs, yshift=0mm] {\colorbox{blue!15}{$\Delta G_{SVP}$=-9.98}\\ \colorbox{red!15}{$\Delta G_{TZVPD}$=-7.27}\\\colorbox{green!15}{$ \Delta G_{DMF}$=-6.80}}
    node[svp_mol] {\ce{CH3Cl \bond{...}Br-}} 
    node[svp_desc] {$\Delta G$=-9.98} 
    -- ++(1,0);
    
    \draw[svp_reac] (11, -9.98) -- (12, -6.40);
    
    \draw[svp_level] (12,-6.40) -- ++(1,0) 
    node[gibbs, yshift=-1mm] {\colorbox{blue!15}{$\Delta G_{SVP}$=-6.40}\\ \colorbox{red!15}{$\Delta G_{TZVPD}$=9.93}\\\colorbox{green!15}{$ \Delta G_{DMF}$=-0.12}}
    node[svp_mol] {\ce{CH3Cl + Br-}} 
    node[svp_desc] {$\Delta G$=-6.40} 
    -- ++(1,0);
    
    %%%%%% TZVPD
    \draw[tzvpd_level] (0,18.12) -- ++(1,0) 
    node[tzvpd_mol] {\chemfig{Cl^{-}}\qquad \chemfig{C(-[:120]H)(<[:-110]H)(<:[:-130]H)-Br}} 
    node[tzvpd_desc] {$\Delta G$=18.12} -- ++(1,0);
    \draw[tzvpd_reac] (2, 18.12) -- (3, 0);
    \draw[tzvpd_level] (3,0) -- ++(1,0) 
    %node[tzvpd_mol] {\ce{Cl- \bond{...} CH3Br}}
    node[tzvpd_desc] {$\Delta G$=0} -- ++(1,0);
    \draw[tzvpd_reac] (5,0) -- (6, 4.88); 
    \draw[tzvpd_level] (6,4.88) -- ++(1,0) 
    %node[tzvpd_mol] {\ce{[Cl\bond{...}CH3 \bond{...}Br]-}} 
    node[tzvpd_desc] {$\Delta G$=4.88} -- ++(1,0);
    \draw[tzvpd_reac] (8,4.88) -- (9, -7.27);
    \draw[tzvpd_level] (9,-7.272975) -- ++(1,0) 
    %node[tzvpd_mol] {\ce{CH3Cl \bond{...}Br-}} 
    node[tzvpd_desc] {$\Delta G$=-7.27} -- ++(1,0);
    \draw[tzvpd_reac] (11, -7.27) -- (12, 9.93);
    \draw[tzvpd_level] (12,9.93) -- ++(1,0) 
    node[tzvpd_mol] {\chemfig{Cl-C(-[:60]H)(<[:-50]H)(<:[:-70]H)}\qquad\chemfig{Br^{-}}} 
    node[tzvpd_desc] {$\Delta G$=9.93} -- ++(1,0);
    
    %%%%%% DMF
    \draw[dmf_level] (0,3.497715) -- ++(1,0) 
    node[gibbs, yshift=-6mm] {\colorbox{blue!15}{$\Delta G_{SVP}$=11.91}\\ \colorbox{red!15}{$\Delta G_{TZVPD}$=18.12}\\\colorbox{green!15}{$ \Delta G_{DMF}$=3.50}}
    %node[dmf_mol] {\chemfig{Cl^{-}}\qquad \chemfig{C(-[:120]H)(<[:-110]H)(<:[:-130]H)-Br}} 
    node[dmf_desc] {$\Delta G$=3.497715} -- ++(1,0);
    
    \draw[dmf_reac] (2, 3.497715) -- (3, 0);
    
    \draw[dmf_level] (3,0) -- ++(1,0) 
    node[gibbs, yshift=-1mm] {\colorbox{blue!15}{$\Delta G_{SVP}$=0}\\ \colorbox{red!15}{$\Delta G_{TZVPD}$=0}\\\colorbox{green!15}{$ \Delta G_{DMF}$=0}}
    node[dmf_mol] {\chemfig{Cl^{-}-[,,,,dash pattern=on 2pt off 2pt]C(-[:120]H)(<[:-110]H)(<:[:-130]H)-Br}}
    node[dmf_desc] {$\Delta G$=0} -- ++(1,0);
    
    \draw[dmf_reac] (5,0) -- (6, 10.02); 
    
    \draw[dmf_level] (6,10.02) -- ++(1,0) 
    node[dmf_mol] {\chemleft[\chemfig{Cl-[,,,,dash pattern=on 2pt off 2pt]C(-[:90]H)(<[:-75]H)(<:[:-105]H)-[,,,,dash pattern=on 2pt off 2pt]Br}\chemright]$^{-}$} 
    node[dmf_desc] {$\Delta G$=10.02} -- ++(1,0);
    
    \draw[dmf_reac] (8,10.02) -- (9, -6.80);
    
    \draw[dmf_level] (9,-6.80) -- ++(1,0) 
    node[dmf_mol] {\chemfig{Cl-C(-[:60]H)(<[:-50]H)(<:[:-70]H)-[,,,,dash pattern=on 2pt off 2pt]Br^{-}}} 
    node[dmf_desc] {$\Delta G$=-6.80} -- ++(1,0);
    
    \draw[dmf_reac] (11, -6.80) -- (12, -0.116734);
    
    \draw[dmf_level] (12,-0.116734) -- ++(1,0) 
    %node[dmf_mol] {\chemfig{Cl-C(-[:60]H)(<[:-50]H)(<:[:-70]H)}\qquad\chemfig{Br^{-}}} 
    node[dmf_desc] {$\Delta G$=-0.116734} -- ++(1,0);
    
    \end{tikzpicture}
    \caption{Reaction diagram for the three methods studied: B3LYP/Def2-SVP (blue), B3LYP/Def2-TZVPD (red), B3LYP/Def2-TZVPD with CPCM(DMF) (green). All units in kcal/mol.}
    \label{fig:reaction diagram all in one}
\end{figure}"""