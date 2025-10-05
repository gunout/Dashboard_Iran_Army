# dashboard_defense_iran_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Iran",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #239F40, #FFFFFF, #DA0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #239F40, #1A7A32);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #DA0000;
        border-bottom: 3px solid #239F40;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .missile-card {
        background: linear-gradient(135deg, #DA0000, #B22222);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-defense-card {
        background: linear-gradient(135deg, #008080, #00CED1);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .asymmetric-card {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .proxy-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseIranDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.missile_systems = self.define_missile_systems()
        self.naval_assets = self.define_naval_assets()
        
    def define_branches_options(self):
        return [
            "Forces Armées de la RII", "Armée de Terre", "Marine de la RII", 
            "Force Aérienne", "Forces de la Révolution Islamique (IRGC)",
            "Forces Quds", "Basij", "Garde Côtière"
        ]
    
    def define_programmes_options(self):
        return [
            "Programme Missilistique", "Défense Aérienne", 
            "Capacités Navales Asymétriques", "Guerre de Proximité",
            "Cybersécurité", "Drones de Combat", "Programme Nucléaire"
        ]
    
    def define_missile_systems(self):
        return {
            "Shahab-3": {"type": "MRBM", "portee": 2000, "precision": "50m", "statut": "Opérationnel"},
            "Ghadr": {"type": "MRBM", "portee": 1600, "precision": "30m", "statut": "Opérationnel"},
            "Emad": {"type": "MRBM", "portee": 1700, "precision": "500m", "statut": "Opérationnel"},
            "Sejjil": {"type": "MRBM", "portee": 2000, "precision": "100m", "statut": "Test"},
            "Khorramshahr": {"type": "MRBM", "portee": 2000, "precision": "80m", "statut": "Opérationnel"},
            "Fateh-110": {"type": "Missile Sol-Sol", "portee": 300, "precision": "10m", "statut": "Opérationnel"}
        }
    
    def define_naval_assets(self):
        return {
            "Sous-marin Classe Ghadir": {"type": "Sous-marin de poche", "deplacement": 120, "torpilles": 2, "statut": "Opérationnel"},
            "Sous-marin Classe Fateh": {"type": "Sous-marin conventionnel", "deplacement": 600, "missiles": "Croisière", "statut": "Opérationnel"},
            "Vedette Tondar": {"type": "Vedette rapide", "deplacement": 12, "missiles": "Anti-navires", "statut": "Opérationnel"},
            "Navire Moudge": {"type": "Frégate", "deplacement": 1500, "missiles": "Surface-air", "statut": "Opérationnel"},
            "Navire logistique Bandar Abbas": {"type": "Navire soutien", "deplacement": 45000, "capacite": "Ravitaillement", "statut": "Opérationnel"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour l'Iran"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Tests_Missiles': self.simulate_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'missiles' in config.get('priorites', []):
            data.update({
                'Stock_Missiles': self.simulate_missile_arsenal_size(annees),
                'Portee_Max_Missiles_Km': self.simulate_missile_range_evolution(annees),
                'Precision_Missiles': self.simulate_missile_accuracy(annees),
                'Production_Missiles_An': self.simulate_missile_production(annees)
            })
        
        if 'asymetrique' in config.get('priorites', []):
            data.update({
                'Forces_Proxies': self.simulate_proxy_forces(annees),
                'Capacite_Navale_Asymetrique': self.simulate_asymmetric_naval(annees),
                'Exercices_Guerre_Proximite': self.simulate_swarm_exercises(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Capacite_Enrichissement': self.simulate_enrichment_capacity(annees),
                'Centrifuges_Operationnels': self.simulate_centrifuges(annees),
                'Expertise_Nucleaire': self.simulate_nuclear_expertise(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour l'Iran"""
        configs = {
            "Forces Armées de la RII": {
                "type": "armee_totale",
                "budget_base": 15.0,
                "personnel_base": 610,
                "exercices_base": 80,
                "priorites": ["missiles", "asymetrique", "cyber", "nucleaire", "defense_aerienne"],
                "doctrines": ["Dissuasion Asymétrique", "Guerre de Proximité", "Défense Stratégique"],
                "capacites_speciales": ["Essaims de vedettes", "Missiles balistiques", "Guerre cyber"]
            },
            "Forces de la Révolution Islamique (IRGC)": {
                "type": "branche_elite",
                "personnel_base": 125,
                "exercices_base": 45,
                "priorites": ["missiles_balistiques", "operations_speciales", "proxies", "cyber"],
                "unites_speciales": ["Forces Quds", "Basij", "Forces Navales IRGC"],
                "zones_operations": ["Moyen-Orient", "Golfe Persique", "Mer d'Oman"]
            },
            "Programme Missilistique": {
                "type": "programme_strategique",
                "budget_base": 3.5,
                "priorites": ["missiles_balistiques", "missiles_croisiere", "precision", "portee"],
                "systemes_deployes": ["Shahab-3", "Ghadr", "Emad", "Fateh-110"],
                "objectifs": "Couverture régionale complète"
            },
            "Capacités Navales Asymétriques": {
                "type": "programme_asymetrique",
                "budget_base": 1.2,
                "priorites": ["sous_marins", "vedettes_rapides", "mines_marines", "missiles_anti_navires"],
                "capacites": ["Essaims navals", "Guerre des détroits", "Déni d'accès"],
                "zones": ["Détroit d'Ormuz", "Golfe Persique"]
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 50,
            "exercices_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 12.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.045 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2006 <= annee <= 2008:  # Tensions nucléaires
                base *= 1.1
            elif 2010 <= annee <= 2012:  # Sanctions renforcées
                base *= 0.9
            elif annee >= 2015:  # Levée partielle des sanctions
                base *= 1.15
            elif annee >= 2018:  # Retrait américain JCPOA
                base *= 1.1
            elif annee >= 2020:  # Tensions régionales
                base *= 1.2
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 500)
        return [personnel_base * (1 + 0.012 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [3.2 + 0.15 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 60)
        return [base + 4 * (annee - 2000) + 6 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 70 + 1.3 * (annee - 2000)
            if annee >= 2006:  # Préparation face aux menaces
                base += 5
            if annee >= 2011:  # Expérience régionale
                base += 6
            if annee >= 2015:  # Modernisation
                base += 4
            readiness.append(min(base, 92))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            if annee < 2000:
                base = 40  # Capacités conventionnelles
            elif annee < 2008:
                base = 55  # Développement missiles
            elif annee < 2015:
                base = 70  # Capacités régionales
            else:
                base = 80 + 1.5 * (annee - 2015)  # Dissuasion avancée
            deterrence.append(min(base, 95))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(30 - 0.8 * (annee - 2000), 7) for annee in annees]
    
    def simulate_missile_tests(self, annees):
        """Tests de missiles"""
        tests = []
        for annee in annees:
            if annee < 2005:
                tests.append(2)
            elif annee < 2010:
                tests.append(5 + (annee - 2005))
            elif annee < 2015:
                tests.append(10 + 2 * (annee - 2010))
            else:
                tests.append(20 + 3 * (annee - 2015))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(45 + 2.8 * (annee - 2000), 85) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(75 + 1.5 * (annee - 2000), 92) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(50 + 2.5 * (annee - 2000), 88) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(65 + 2.2 * (annee - 2000), 90) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(55 + 3.2 * (annee - 2000), 87) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(60 + 2.5 * (annee - 2000), 89) for annee in annees]
    
    def simulate_missile_arsenal_size(self, annees):
        """Évolution du stock de missiles"""
        stock = []
        for annee in annees:
            if annee < 2000:
                stock.append(100)
            elif annee < 2008:
                stock.append(200 + 30 * (annee - 2000))
            elif annee < 2015:
                stock.append(500 + 50 * (annee - 2008))
            else:
                stock.append(1000 + 80 * (annee - 2015))
        return [min(s, 3000) for s in stock]
    
    def simulate_missile_range_evolution(self, annees):
        """Évolution de la portée maximale des missiles"""
        portee = []
        for annee in annees:
            if annee < 2000:
                portee.append(300)  # Scud
            elif annee < 2006:
                portee.append(500 + 100 * (annee - 2000))  # Shahab-1/2
            elif annee < 2012:
                portee.append(1300 + 150 * (annee - 2006))  # Shahab-3
            else:
                portee.append(2000)  # Missiles à moyenne portée
        return portee
    
    def simulate_missile_accuracy(self, annees):
        """Amélioration de la précision des missiles"""
        return [max(1000 - 40 * (annee - 2000), 50) for annee in annees]
    
    def simulate_missile_production(self, annees):
        """Production annuelle de missiles"""
        return [min(50 + 10 * (annee - 2000), 200) for annee in annees]
    
    def simulate_proxy_forces(self, annees):
        """Forces proxy soutenues"""
        return [min(5 + 2 * (annee - 2000), 50) for annee in annees]
    
    def simulate_asymmetric_naval(self, annees):
        """Capacités navales asymétriques"""
        return [min(40 + 3 * (annee - 2000), 85) for annee in annees]
    
    def simulate_swarm_exercises(self, annees):
        """Exercices de guerre d'essaims"""
        return [min(10 + 2 * (annee - 2000), 60) for annee in annees]
    
    def simulate_enrichment_capacity(self, annees):
        """Capacité d'enrichissement d'uranium"""
        return [min(5 + 3 * (annee - 2000), 40) for annee in annees]
    
    def simulate_centrifuges(self, annees):
        """Centrifuges opérationnels (milliers)"""
        return [min(1 + 0.5 * (annee - 2000), 20) for annee in annees]
    
    def simulate_nuclear_expertise(self, annees):
        """Expertise nucléaire"""
        return [min(30 + 4 * (annee - 2000), 85) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [min(15 + 3 * (annee - 2000), 80) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(50 + 3 * (annee - 2000), 88) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(45 + 3.2 * (annee - 2000), 86) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">☪️ ANALYSE STRATÉGIQUE AVANCÉE - RÉPUBLIQUE ISLAMIQUE D\'IRAN</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #239F40, #DA0000); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ SYSTÈME DE DÉFENSE INTÉGRÉ DE LA RÉPUBLIQUE ISLAMIQUE D'IRAN</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Forces Armées de la RII"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Tensions Régionales", "Sanctions Renforcées", "Conflit Ouvert"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="missile-card">
                <h4>🚀 ARSENAL MISSILISTIQUE</h4>
                <h2>{:.0f}%</h2>
                <p>🎯 {} missiles stratégiques</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Missiles', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="asymmetric-card">
                <h4>🌊 CAPACITÉS ASYMÉTRIQUES</h4>
                <h2>{:.0f}%</h2>
                <p>⚡ {} groupes proxy</p>
            </div>
            """.format(data_actuelle.get('Capacite_Navale_Asymetrique', 0), 
                     int(data_actuelle.get('Forces_Proxies', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_AD'] - data_2000['Couverture_AD']) / 
                           data_2000['Couverture_AD']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_AD']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Portee_Max_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Max_Missiles_Km'] - data_2000.get('Portee_Max_Missiles_Km', 300)) / 
                                   data_2000.get('Portee_Max_Missiles_Km', 300)) * 100
                st.metric(
                    "🎯 Portée Missiles Max",
                    f"{data_actuelle['Portee_Max_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_AD']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Défense Anti-Aérienne']
            couleurs = ['#239F40', '#DA0000', '#2d3436', '#4B0082']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Stock_Missiles' in df.columns:
                strategic_data.append(df['Stock_Missiles'] / 10)  # Normalisation
                strategic_names.append('Stock Missiles (x10)')
            
            if 'Tests_Missiles' in df.columns:
                strategic_data.append(df['Tests_Missiles'])
                strategic_names.append('Tests de Missiles')
            
            if 'Forces_Proxies' in df.columns:
                strategic_data.append(df['Forces_Proxies'])
                strategic_names.append('Groupes Proxy')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des zones d'influence
            st.markdown("""
            <div class="missile-card">
                <h4>🎯 AXE DE RÉSISTANCE ET ZONES D'INFLUENCE</h4>
                <p><strong>Liban:</strong> Hezbollah - 100,000+ missiles</p>
                <p><strong>Syrie:</strong> Présence militaire et milices</p>
                <p><strong>Irak:</strong> Milices Hashd al-Shaabi</p>
                <p><strong>Yémen:</strong> Houthis - contrôle stratégique</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="asymmetric-card">
                <h4>🌐 RELATIONS INTERNATIONALES</h4>
                <p><strong>États-Unis:</strong> Opposition stratégique</p>
                <p><strong>Israël:</strong> Adversaire régional principal</p>
                <p><strong>Arabie Saoudite:</strong> Rivalité régionale</p>
                <p><strong>Russie/Chine:</strong> Partenaires stratégiques</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des sanctions
            sanctions_data = {
                'Année': [2006, 2010, 2012, 2015, 2018, 2020, 2022],
                'Sanctions': ['Résolution 1737', 'Résolution 1929', 'Embargo pétrolier', 
                            'JCPOA Temporaire', 'Retrait US JCPOA', 'Maximum Pressure', 'Nouvelles sanctions'],
                'Impact': [5, 7, 8, 3, 7, 9, 8]  # sur 10
            }
            sanctions_df = pd.DataFrame(sanctions_data)
            
            fig = px.bar(sanctions_df, x='Année', y='Impact', 
                        title="📉 IMPACT DES SANCTIONS INTERNATIONALES",
                        labels={'Impact': 'Niveau d\'Impact'},
                        color='Impact',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice d'autosuffisance
            autosuffisance = [min(40 + 3 * (annee - 2000), 85) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=autosuffisance,
                         title="🛠️ AUTOSUFFISANCE MILITAIRE - RÉSILIENCE FACE AUX SANCTIONS",
                         labels={'x': 'Année', 'y': 'Niveau d\'Autosuffisance (%)'})
            fig.update_traces(fillcolor='rgba(218, 0, 0, 0.3)', line_color='#DA0000')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['Shahab-3', 'Ghadr', 'Fateh-110', 'Sous-marin Ghadir', 
                           'Vedette Tondar', 'Drone Shahed-129', 'Bavar-373'],
                'Portée (km)': [2000, 1600, 300, 3000, 200, 2000, 200],
                'Année Service': [2003, 2007, 2002, 2007, 2002, 2012, 2019],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Missiles Balistiques', 'Défense Aérienne', 
                          'Marine Asymétrique', 'Drones', 'Cyberguerre'],
                'Niveau 2000': [40, 30, 35, 20, 25],
                'Niveau 2027': [85, 75, 80, 70, 75]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#239F40'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#DA0000'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="missile-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Détroit d'Ormuz:</strong> Point de contrôle maritime</p>
                <p><strong>Bushehr:</strong> Centrale nucléaire</p>
                <p><strong>Natanz/Fordow:</strong> Sites d'enrichissement</p>
                <p><strong>Bandar Abbas:</strong> Base navale principale</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="missile-card">
                <h4>🎯 DOCTRINE DE DÉFENSE STRATÉGIQUE</h4>
                <p><strong>Dissuasion asymétrique:</strong> Coût inacceptable pour l'ennemi</p>
                <p><strong>Défense en profondeur:</strong> Multiples lignes défensives</p>
                <p><strong>Riposte massive:</strong> Frappes sur intérêts adverses</p>
                <p><strong>Résilience:</strong> Capacité à absorber les frappes</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="asymmetric-card">
                <h4>⚡ DOCTRINE DE GUERRE ASYMÉTRIQUE</h4>
                <p><strong>Guerre de proximité:</strong> Combat rapproché</p>
                <p><strong>Essaims navals:</strong> Tactiques de saturation</p>
                <p><strong>Forces proxy:</strong> Délégation du combat</p>
                <p><strong>Guerre économique:</strong> Contrôle des détroits</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="proxy-card">
                <h4>🌐 STRATÉGIE RÉGIONALE</h4>
                <p><strong>Axe de Résistance:</strong> Réseau d'alliances</p>
                <p><strong>Projection de puissance:</strong> Influence régionale</p>
                <p><strong>Guerre par procuration:</strong> Conflits indirects</p>
                <p><strong>Négation d'accès:</strong> Contrôle des voies maritimes</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="navy-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES IRANIENNES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Décentralisation:</strong> Commandement flexible</div>
                <div><strong>• Mobilité et surprise:</strong> Opérations rapides</div>
                <div><strong>• Utilisation du terrain:</strong> Connaissance locale</div>
                <div><strong>• Guerre psychologique:</strong> Impact moral</div>
                <div><strong>• Coordination politico-militaire:</strong> Unité d'action</div>
                <div><strong>• Résilience logistique:</strong> Autosuffisance</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Frappe Israélienne', 'Intervention US', 'Guerre Navale', 
                                 'Cyber Attaque', 'Soulèvement Interne', 'Blocus Économique'],
                'Probabilité': [0.6, 0.4, 0.5, 0.8, 0.3, 0.7],
                'Impact': [0.8, 0.9, 0.7, 0.6, 0.8, 0.9],
                'Niveau Préparation': [0.9, 0.7, 0.8, 0.6, 0.5, 0.8]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Attaque Aérienne', 'Blocus Naval', 'Cyber Attaque', 
                           'Opérations Spéciales', 'Guerre Régionale'],
                'Missiles': [0.9, 0.7, 0.2, 0.6, 0.8],
                'Marine': [0.4, 0.9, 0.1, 0.3, 0.6],
                'Proxies': [0.3, 0.2, 0.1, 0.8, 0.7],
                'Cyber': [0.2, 0.1, 0.9, 0.4, 0.5]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Missiles', x=response_df['Scénario'], y=response_df['Missiles']),
                go.Bar(name='Marine', x=response_df['Scénario'], y=response_df['Marine']),
                go.Bar(name='Proxies', x=response_df['Scénario'], y=response_df['Proxies']),
                go.Bar(name='Cyber', x=response_df['Scénario'], y=response_df['Cyber'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="missile-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement missilistique:</strong> Portée et précision</div>
                <div><strong>• Défense aérienne:</strong> Systèmes intégrés</div>
                <div><strong>• Capacités navales:</strong> Guerre asymétrique</div>
                <div><strong>• Cyber guerre:</strong> Offensive et défensive</div>
                <div><strong>• Forces proxy:</strong> Élargissement réseau</div>
                <div><strong>• Autosuffisance:</strong> Production indigène</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_missile_database(self):
        """Base de données des systèmes de missiles"""
        st.markdown('<h3 class="section-header">🚀 BASE DE DONNÉES DES SYSTÈMES DE MISSILES</h3>', 
                   unsafe_allow_html=True)
        
        missile_data = []
        for nom, specs in self.missile_systems.items():
            missile_data.append({
                'Système': nom,
                'Type': specs['type'],
                'Portée (km)': specs['portee'],
                'Précision': specs['precision'],
                'Statut': specs['statut'],
                'Classification': 'Stratégique' if specs['portee'] > 1000 else 'Tactique'
            })
        
        missile_df = pd.DataFrame(missile_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(missile_df, x='Portée (km)', y='Précision',
                           size='Portée (km)', color='Classification',
                           hover_name='Système', log_x=True,
                           title="🚀 CARACTÉRISTIQUES DES SYSTÈMES DE MISSILES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="missile-card">
                <h4>📋 INVENTAIRE MISSILISTIQUE</h4>
            """, unsafe_allow_html=True)
            
            for missile in missile_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{missile['Système']}</strong><br>
                    🎯 {missile['Type']} • 🚀 {missile['Portée (km)']:,} km<br>
                    📏 {missile['Précision']} • {missile['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "🚀 Systèmes de Missiles",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_missile_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - RÉPUBLIQUE ISLAMIQUE D\'IRAN</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="missile-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="asymmetric-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Puissance Missilistique Régionale</strong>
                        <p>Le plus grand arsenal de missiles du Moyen-Orient avec couverture régionale complète</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🌊 Contrôle des Détroits Stratégiques</strong>
                        <p>Capacité de fermer le détroit d'Ormuz, voie vitale pour le pétrole mondial</p>
                    </div>
                    <div class="proxy-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Réseau d'Alliances Régionales</strong>
                        <p>Axe de Résistance étendu à travers le Moyen-Orient avec forces proxy entraînées</p>
                    </div>
                    <div class="cyber-card" style="margin: 0.5rem 0;">
                        <strong>💻 Capacités Cyber Avancées</strong>
                        <p>Expertise reconnue en cyber guerre offensive et défensive</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="asymmetric-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="asymmetric-card" style="margin: 0.5rem 0;">
                        <strong>💸 Impact des Sanctions</strong>
                        <p>Sanctions économiques limitant l'accès aux technologies et financements</p>
                    </div>
                    <div class="asymmetric-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Obsolescence Technologique</strong>
                        <p>Équipements conventionnels vieillissants face à des adversaires modernes</p>
                    </div>
                    <div class="asymmetric-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Isolement Diplomatique</strong>
                        <p>Relations limitées avec les puissances occidentales et arabes</p>
                    </div>
                    <div class="asymmetric-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Dépendance aux Importations</strong>
                        <p>Certains composants militaires critiques encore importés</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DOMAINE MISSILISTIQUE</h5>
                    <p>• Missiles à très longue portée<br>• Têtes multiples (MIRV)<br>• Systèmes hypersoniques<br>• Satellites de reconnaissance</p>
                </div>
                <div>
                    <h5>🌊 CAPACITÉS NAVALES</h5>
                    <p>• Porte-avions légers<br>• Sous-marins conventionnels avancés<br>• Drones navals<br>• Systèmes de mines intelligentes</p>
                </div>
                <div>
                    <h5>💻 TECHNOLOGIES AVANCÉES</h5>
                    <p>• Drones de combat longue portée<br>• Guerre électronique avancée<br>• Cyber commandement unifié<br>• Défense antimissile intégrée</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="missile-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Modernisation continue des missiles<br>
                    • Renforcement de la défense aérienne<br>
                    • Développement des capacités navales asymétriques<br>
                    • Expansion du réseau de proxies</p>
                </div>
                <div>
                    <h5>⚡ DISSUASION AVANCÉE</h5>
                    <p>• Diversification des vecteurs de frappe<br>
                    • Renforcement des capacités cyber offensives<br>
                    • Développement capacités spatiales<br>
                    • Coopération avec partenaires stratégiques</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseIranDashboardAvance()
    dashboard.run_advanced_dashboard()