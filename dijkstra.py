import heapq

def dijkstra(graph, start):
    # Khởi tạo mảng chứa khoảng cách ngắn nhất từ đỉnh nguồn đến các đỉnh khác.
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0
    
    # Khởi tạo hàng đợi ưu tiên sử dụng module heapq của Python.
    pq = [(0, start)]
    
    while pq:
        # Lấy đỉnh có khoảng cách ngắn nhất tồn tại trong hàng đợi.
        (dist, current_node) = heapq.heappop(pq)
        
        # Nếu đỉnh này đã được xét rồi thì ta bỏ qua.
        if dist > distances[current_node]:
            continue
        
        # Duyệt qua các đỉnh kề với đỉnh hiện tại.
        for neighbor, weight in graph[current_node].items():
            # Tính toán khoảng cách mới từ đỉnh nguồn đến đỉnh kề.
            distance = dist + weight
            
            # Nếu khoảng cách mới tốt hơn khoảng cách hiện tại thì cập nhật lại và đánh dấu đỉnh cha của đỉnh kề.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
