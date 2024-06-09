import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import filedialog
import time

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Editor")
        self.master.minsize(800, 400)
        self.graph = nx.Graph()

        #===========================  Canvas  ===================================
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas_ntk = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas_ntk.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #=========================================================================

        #===========================  Vértice  ===================================
        self.verticeDiv = tk.Frame(master)
        self.verticeDiv.pack(expand = False, fill = "both")

        self.verticeLabel = tk.Label(self.verticeDiv, text="Vértice")
        self.verticeLabel.pack(padx = 5, pady = 1, expand = False, fill = "x")

        self.verticeEntry = tk.Entry(self.verticeDiv, justify='center')
        self.verticeEntry.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.verticeButtons = tk.Frame(self.verticeDiv)
        self.verticeButtons.pack(expand = False, fill = "x")

        self.add_button = tk.Button(self.verticeButtons, text="Adicionar", command=self.add_vertex)
        self.add_button.pack(side="left", expand = True, padx=5, pady=5, fill = "both") 
        self.remove_button = tk.Button(self.verticeButtons, text="Remover", command=self.remove_vertex)
        self.remove_button.pack(side="left", expand = True, padx=5, pady=5, fill = "both")
        #=========================================================================

        self.edge_label = tk.Label(master, text="Aresta (Origem-Destino):")
        self.edge_label.pack(padx = 5, pady = 1, expand = False, fill = "both")
        self.edge_origin_entry = tk.Entry(master)
        self.edge_origin_entry.pack(padx = 5, pady = 1, expand = False, fill = "both")
        self.edge_dest_entry = tk.Entry(master)
        self.edge_dest_entry.pack(padx = 5, pady = 1, expand = False, fill = "both")
        self.edge_button = tk.Button(master, text="Adicionar Aresta", command=self.add_edge)
        self.edge_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.load_button = tk.Button(master, text="Carregar Grafo", command=self.load_graph)
        self.load_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.save_button = tk.Button(master, text="Salvar Grafo", command=self.save_graph)
        self.save_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.percorrerV_button = tk.Button(master, text="Percorrer Vertice", command=self.percorrer_vertice)
        self.percorrerV_button.pack(padx = 5, pady = 1, expand = False, fill = "both")

        self.percorrerA_button = tk.Button(master, text="Percorrer Aresta", command=self.percorrer_aresta)
        self.percorrerA_button.pack(padx = 5, pady = 1, expand = False, fill = "both")
        
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
            pos = nx.planar_layout(self.graph)
            nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_size=500, node_color=color_map)
            self.printLog(f'Vertice {node}')
            self.canvas_ntk.draw()
            self.master.update_idletasks()
            time.sleep(1)

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
            pos = nx.planar_layout(self.graph)
            self.printLog(f'Arésta {edgeor} <--> {edgedes}')
            nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_size=500, edge_color=color_map, node_color='skyblue')
            self.canvas_ntk.draw()
            self.master.update_idletasks()
            time.sleep(1)

    def add_edge(self):
        origin = self.edge_origin_entry.get()
        dest = self.edge_dest_entry.get()
        if origin and dest:
            self.graph.add_edge(origin, dest)
            self.draw_graph()
            self.edge_origin_entry.delete(0, tk.END)
            self.edge_dest_entry.delete(0, tk.END)
            self.printLog(f'Arésta {origin} <--> {dest} criada com sucesso.')

    def load_graph(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            df = pd.read_csv(filename)
            self.graph = nx.from_pandas_edgelist(df)
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
        pos = nx.planar_layout(self.graph)
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_size=500, node_color='skyblue')
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
