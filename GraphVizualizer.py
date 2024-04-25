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

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas_ntk = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas_ntk.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.add_label = tk.Label(master, text="Vértice:")
        self.add_label.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.add_entry = tk.Entry(master)
        self.add_entry.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.add_button = tk.Button(master, text="Adicionar Vértice", command=self.add_vertex)
        self.add_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.remove_label = tk.Label(master, text="Vértice a Remover:")
        self.remove_label.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.remove_entry = tk.Entry(master)
        self.remove_entry.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.remove_button = tk.Button(master, text="Remover Vértice", command=self.remove_vertex)
        self.remove_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.edge_label = tk.Label(master, text="Aresta (Origem-Destino):")
        self.edge_label.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.edge_origin_entry = tk.Entry(master)
        self.edge_origin_entry.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.edge_dest_entry = tk.Entry(master)
        self.edge_dest_entry.pack(padx = 2, pady = 1, expand = False, fill = "both")
        self.edge_button = tk.Button(master, text="Adicionar Aresta", command=self.add_edge)
        self.edge_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.load_button = tk.Button(master, text="Carregar Grafo", command=self.load_graph)
        self.load_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.save_button = tk.Button(master, text="Salvar Grafo", command=self.save_graph)
        self.save_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.percorrerV_button = tk.Button(master, text="Percorrer Vertice", command=self.percorrer_vertice)
        self.percorrerV_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.save_button = tk.Button(master, text="Percorrer Aresta", command=self.save_graph)
        self.save_button.pack(padx = 2, pady = 1, expand = False, fill = "both")

        self.draw_graph()

    def add_vertex(self):
        vertex = self.add_entry.get()
        if vertex:
            self.graph.add_node(vertex)
            self.draw_graph()
            self.add_entry.delete(0, tk.END)

    def remove_vertex(self):
        vertex = self.remove_entry.get()
        if vertex:
            if vertex in self.graph.nodes():
                self.graph.remove_node(vertex)
                self.draw_graph()
            else:
                print("Vértice não encontrado.")
            self.remove_entry.delete(0, tk.END)

    def percorrer_vertice(self):
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

    def load_graph(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            df = pd.read_csv(filename)
            self.graph = nx.from_pandas_edgelist(df)
            self.draw_graph()

    def save_graph(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            df = nx.to_pandas_edgelist(self.graph)
            df.to_csv(filename, index=False)

    def draw_graph(self):
        self.ax.clear()
        pos = nx.planar_layout(self.graph)
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_size=500, node_color='skyblue')
        self.canvas_ntk.draw()


def main():
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
