import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import time


class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Editor")
        self.master.minsize(800, 400)
        self.graph = nx.Graph()

        self.pos = {}

        default_font = tkFont.Font(family="Arial", size=10, weight="normal", slant="roman")
        title_font = tkFont.Font(family="Arial", size=12, weight="normal", slant="roman")

        #===========================  Canvas  ===================================
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas_ntk = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas_ntk.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #=========================================================================

        #===========================  Vértice  ===================================
        self.verticeDiv = tk.Frame(master)
        self.verticeDiv.pack(expand = False, fill = "both")

        self.verticeLabel = tk.Label(self.verticeDiv, text="Vértice", font = title_font)
        self.verticeLabel.pack(padx = 5, pady = 1, expand = False, fill = "x")
        self.verticeEntry = tk.Entry(self.verticeDiv, justify='center')
        self.verticeEntry.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.verticeButtons = tk.Frame(self.verticeDiv)
        self.verticeButtons.pack(expand = False, fill = "x")

        self.add_button = tk.Button(self.verticeButtons, text="Adicionar", command=self.add_vertex, font = default_font)
        self.add_button.pack(side="left", expand = True, padx=5, pady=5, fill = "both") 
        self.remove_button = tk.Button(self.verticeButtons, text="Remover", command=self.remove_vertex, font = default_font)
        self.remove_button.pack(side="left", expand = True, padx=5, pady=5, fill = "both")
        self.removeall_button = tk.Button(master, text="Apagar todos", command=self.remove_Allvertex, font = default_font)
        self.removeall_button.pack(padx = 5, pady = 1, expand = False, fill = "both")
        #=========================================================================

        #===========================  Arestas  ===================================
        self.arestaDiv = tk.Frame(master)
        self.arestaDiv.pack(expand = False, fill = "both")

        self.edge_label = tk.Label(self.arestaDiv, text="Aresta", font = title_font)
        self.edge_label.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.arestaEntry1 = tk.Frame(self.arestaDiv)
        self.arestaEntry1.pack(expand = False, fill = "x")
        self.edge_origin_label = tk.Label(self.arestaEntry1, text="Origem:", font = default_font)
        self.edge_origin_label.pack(side="left", expand = False, padx = 5, pady = 1)
        self.edge_origin_entry = tk.Entry(self.arestaEntry1, justify='center')
        self.edge_origin_entry.pack(side="left", expand = True, padx = 5, pady = 1, fill = "both")

        self.arestaEntry2 = tk.Frame(self.arestaDiv)
        self.arestaEntry2.pack(expand = False, fill = "x")
        self.edge_dest_label = tk.Label(self.arestaEntry2, text="Destino:", font = default_font)
        self.edge_dest_label.pack(side="left", expand = False, padx = 5, pady = 1)
        self.edge_dest_entry = tk.Entry(self.arestaEntry2, justify='center')
        self.edge_dest_entry.pack(side="left", expand = True, padx = 5, pady = 1, fill = "both")

        self.arestaEntry3 = tk.Frame(self.arestaDiv)
        self.arestaEntry3.pack(expand = False, fill = "x")
        self.edge_origin_label = tk.Label(self.arestaEntry3, text="Peso:", font = default_font)
        self.edge_origin_label.pack(side="left", expand = False, padx = 5, pady = 1)
        self.edge_weight_entry = tk.Entry(self.arestaEntry3, justify='center')
        self.edge_weight_entry.pack(side="left", expand = True, padx = 5, pady = 1, fill = "both")

        self.edge_button = tk.Button(self.arestaDiv, text="Adicionar Aresta", command=self.add_edge, font = default_font)
        self.edge_button.pack(expand = False, padx = 5, pady = 5, fill = "both")
        #=========================================================================

        #===========================  Save | Load  ===================================
        self.br = tk.Label(master, text="\nSave | Load", wraplength=200, font = title_font)
        self.br.pack()
        self.load_button = tk.Button(master, text="Carregar Grafo", command=self.load_graph, font = default_font)
        self.load_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.save_button = tk.Button(master, text="Salvar Grafo", command=self.save_graph, font = default_font)
        self.save_button.pack(padx = 5, pady = 1, expand = False, fill = "both")
        #=========================================================================

        #===========================  Métodos  ===================================
        self.br = tk.Label(master, text="\nMétodos", wraplength=200, font = title_font)
        self.br.pack()

        self.percorrerV_button = tk.Button(master, text="Percorrer Vertice", command=self.percorrer_vertice, font = default_font)
        self.percorrerV_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.percorrerA_button = tk.Button(master, text="Percorrer Aresta", command=self.percorrer_aresta, font = default_font)
        self.percorrerA_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.boruvka_button = tk.Button(master, text="Algorítmo de Boruvka", command=self.algoritmo_boruvka, font = default_font)
        self.boruvka_button.pack(padx = 5, pady = 1, expand = False, fill = "both")
        #=========================================================================

        self.log_texto = tk.Text(master, width=40, height=15, state="disabled")
        self.log_texto.pack(padx = 5, pady = 1, expand = True, fill = "both")
        self.draw_graph()

    def add_vertex(self):
        vertex = self.verticeEntry.get()
        if vertex:
            if vertex in self.graph.nodes():
                self.printLog(f'Vértice {vertex} já adicionado.')
            else:
                self.graph.add_node(vertex)
                self.draw_graph()
                self.verticeEntry.delete(0, tk.END)
                self.printLog(f'Vértice {vertex} adicionado com sucesso.')

    def remove_vertex(self):
        vertex = self.verticeEntry.get()
        if vertex:
            if vertex in self.graph.nodes():
                self.graph.remove_node(vertex)
                self.draw_graph()
                self.printLog(f'Vértice {vertex} apagado com sucesso.')
            else:
                self.printLog('Vértice não encontrado.')
            self.verticeEntry.delete(0, tk.END)
    
    def remove_Allvertex(self):
        self.graph.clear()
        self.draw_graph()
        self.printLog(f'Grafo apagado.')

    def add_edge(self):
        origin = self.edge_origin_entry.get()
        dest = self.edge_dest_entry.get()
        peso = self.edge_weight_entry.get()
        if origin and dest and peso:
            self.graph.add_edge(origin, dest, weight = int(peso))
            self.draw_graph()
            self.edge_origin_entry.delete(0, tk.END)
            self.edge_dest_entry.delete(0, tk.END)
            self.edge_weight_entry.delete(0, tk.END)
            self.printLog(f'Arésta {origin} <--> {dest} de peso {peso} criada com sucesso.')

    def percorrer_vertice(self):
        self.printLog('')
        for node in self.graph.nodes:
            color_map = []
            for nodeAlt in self.graph.nodes:
                if node == nodeAlt:
                    color_map.append('red')
                else:
                    color_map.append('skyblue')  
            self.ax.clear()

            options = {
                'node_color': 'skyblue',
                'node_size': 500,
                'node_color': color_map
            }

            labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in self.graph.edges(data=True)])

            nx.draw_networkx(self.graph, self.pos, ax=self.ax, with_labels=True, **options)
            nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = labels)
            self.printLog(f'Vertice {node}')
            self.canvas_ntk.draw()
            self.master.update_idletasks()
            time.sleep(0.3)

    def percorrer_aresta(self):
        self.printLog('')
        for edgeor, edgedes in self.graph.edges:
            color_map = []
            for edgeorAlt, edgedesAlt in self.graph.edges:
                if (edgeor, edgedes) == (edgeorAlt, edgedesAlt):
                    color_map.append('red')
                else:
                    color_map.append('black') 
            self.ax.clear()
            
            options = {
                'node_color': 'skyblue',
                'node_size': 500,
                'edge_color': color_map
            }

            labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in self.graph.edges(data=True)])

            nx.draw_networkx(self.graph, self.pos, ax=self.ax, with_labels=True, **options)
            nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = labels)
            self.printLog(f'Arésta {edgeor} <--> {edgedes}')
            self.canvas_ntk.draw()
            self.master.update_idletasks()
            time.sleep(0.3)
        print(self.graph.edges)

    def algoritmo_boruvka(self):
        janelaResultado = tk.Toplevel(self.master)
        figure = plt.figure()
        ax = figure.add_subplot(111)
        canvas_ntk = FigureCanvasTkAgg(figure, janelaResultado)
        canvas_ntk.get_tk_widget().pack(expand=True)

        minArvoreG = nx.minimum_spanning_tree(self.graph, algorithm='boruvka')
        print(minArvoreG)
        pos = nx.planar_layout(minArvoreG)

        options = {
            'node_color': 'skyblue',
            'node_size': 500,
        }

        labels = dict([((n1, n2), d['weight'])
                    for n1, n2, d in minArvoreG.edges(data=True)])

        nx.draw_networkx(minArvoreG, pos, ax, with_labels=True,**options)
        nx.draw_networkx_edge_labels(minArvoreG, nx.planar_layout(minArvoreG), edge_labels = labels)
        canvas_ntk.draw()

        janelaResultado.deiconify

    def load_graph(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            df = pd.read_csv(filename)
            print(df)
            self.graph = nx.from_pandas_edgelist(df, edge_attr=["weight"])
            self.draw_graph()
            self.printLog(f'Grafo carregado com sucesso.')
        else:
            self.printLog(f'Arquivo desconhecido ou não encontrado.')

    def save_graph(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            df = nx.to_pandas_edgelist(self.graph)
            df.to_csv(filename, index=False)
            self.printLog(f'Grafo salvo com sucesso.')

    def draw_graph(self):
        self.ax.clear()
        self.pos = nx.circular_layout(self.graph)

        options = {
            'node_color': 'skyblue',
            'node_size': 500,
        }

        labels = dict([((n1, n2), d['weight'])
                    for n1, n2, d in self.graph.edges(data=True)])

        nx.draw_networkx(self.graph, self.pos, ax=self.ax, with_labels=True,**options)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = labels)
        self.canvas_ntk.draw()

    def printLog(self, texto):
        self.log_texto.config(state='normal')
        self.log_texto.insert(tk.END, texto + "\n")
        self.log_texto.config(state='disabled')


def main():
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
