import networkx as nx # networkx: Grafik (graph) oluşturmak ve analiz etmek için kullanılır
import matplotlib.pyplot as plt # matplotlib.pyplot: Grafik görselleştirmeleri yapmak için kullanılır

# Yönlü bir grafik oluşturuluyor
G = nx.DiGraph()
nodes = ["A", "B", "C", "D", "E"]

# Düğümler (nodes) tanımlanıyor
G.add_nodes_from(nodes)

edges = [
    ("A", "B", 2),
    ("A", "C", 5),
    ("B", "C", 1),
    ("B", "D", 2),
    ("C", "D", 3),
    ("C", "E", 1),
    ("D", "E", 2),
]

# Tanımlanan kenarlar ve ağırlıkları grafiğe ekleniyor
G.add_weighted_edges_from(edges)

# En kısa yollar
shortest_paths = nx.single_source_dijkstra_path(G, source="A") # En kısa yolun hangi düğümlerden oluştuğu
shortest_distances = nx.single_source_dijkstra_path_length(G, source="A") # En kısa yolun toplam mesafesi

# Sonuçları yazdır
print("A noktasından diğer düğümlere en kısa yollar:")
for target in shortest_paths:
    print(f"A -> {target}: Yol: {shortest_paths[target]}, Mesafe: {shortest_distances[target]}")

# Grafiğin çizileceği pozisyonlar hesaplanıyor
pos = nx.spring_layout(G) # Yayılma (spring) algoritması ile düğümlerin konumları belirleniyor
plt.figure(figsize=(9, 7))

# Düğümler ve kenarlar çiziliyor
nx.draw(G, pos, with_labels=True, node_size=800, node_color="green", font_size=14)

# Kenarların ağırlıkları (etiketleri) alınarak çizime ekleniyor
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Bilgisayar Ağı Grafiği")
plt.show()