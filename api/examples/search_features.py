"""
Примеры использования расширенных возможностей поиска
"""
import requests

API_BASE = "http://localhost:8000"  # Замените на ваш URL API


# 1. Автодополнение
def autocomplete_example():
    """Пример использования автодополнения"""
    print("=" * 60)
    print("1. Автодополнение")
    print("=" * 60)
    
    # Автодополнение по префиксу "под"
    response = requests.get(f"{API_BASE}/autocomplete?q=под")
    if response.status_code == 200:
        data = response.json()
        print(f"\nЗапрос: {data['query']}")
        print(f"Найдено предложений: {data['count']}")
        print("\nПредложения:")
        for suggestion in data['suggestions'][:5]:
            print(f"  - {suggestion['value']} ({suggestion['type']}, частота: {suggestion['frequency']})")
    
    # Автодополнение для кодов подшипников
    print("\n" + "-" * 60)
    response = requests.get(f"{API_BASE}/autocomplete?q=620&types=bearing_code")
    if response.status_code == 200:
        data = response.json()
        print(f"\nЗапрос: {data['query']}")
        print("Предложения (только коды подшипников):")
        for suggestion in data['suggestions'][:5]:
            print(f"  - {suggestion['value']}")
    
    # Популярные термины
    print("\n" + "-" * 60)
    response = requests.get(f"{API_BASE}/autocomplete/popular?limit=5")
    if response.status_code == 200:
        data = response.json()
        print("\nПопулярные термины:")
        for item in data['popular'][:5]:
            print(f"  - {item['value']} ({item['type']})")


# 2. Поиск с похожими документами
def search_with_similar():
    """Пример поиска с похожими документами"""
    print("\n" + "=" * 60)
    print("2. Поиск с похожими документами")
    print("=" * 60)
    
    response = requests.get(f"{API_BASE}/search?q=6205&include_similar=true&limit=3")
    if response.status_code == 200:
        data = response.json()
        print(f"\nЗапрос: {data['query']}")
        print(f"Найдено результатов: {data['total']}")
        
        for i, result in enumerate(data['results'], 1):
            print(f"\n{i}. {result['title']}")
            print(f"   Путь: {result['path']}")
            print(f"   Релевантность: {result['relevance']}")
            
            if 'similar_documents' in result and result['similar_documents']:
                print("   Похожие документы:")
                for sim_doc in result['similar_documents']:
                    print(f"     - {sim_doc['title']} (схожесть: {sim_doc['similarity']})")


# 3. Получение похожих документов
def get_similar_documents():
    """Пример получения похожих документов"""
    print("\n" + "=" * 60)
    print("3. Похожие документы")
    print("=" * 60)
    
    # Сначала делаем поиск, чтобы получить ID документа
    response = requests.get(f"{API_BASE}/search?q=подшипник&limit=1")
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            doc_id = data['results'][0]['id']
            print(f"\nДокумент: {data['results'][0]['title']}")
            
            # Получаем похожие документы
            response = requests.get(f"{API_BASE}/similar/{doc_id}?limit=5")
            if response.status_code == 200:
                similar_data = response.json()
                print(f"\nПохожие документы ({similar_data['count']}):")
                for sim_doc in similar_data['similar']:
                    print(f"  - {sim_doc['title']} (схожесть: {sim_doc['similarity']})")


# 4. История поиска
def search_history():
    """Пример работы с историей поиска"""
    print("\n" + "=" * 60)
    print("4. История поиска")
    print("=" * 60)
    
    user_id = "user123"
    
    # Выполняем несколько поисков
    queries = ["подшипник", "6205", "SKF"]
    for query in queries:
        requests.get(f"{API_BASE}/search?q={query}&user_id={user_id}")
    
    print(f"\nВыполнены запросы: {', '.join(queries)}")
    
    # Получаем историю
    response = requests.get(f"{API_BASE}/history?user_id={user_id}")
    if response.status_code == 200:
        data = response.json()
        print(f"\nИстория пользователя {user_id} ({data['count']} запросов):")
        for entry in data['history']:
            print(f"  - {entry['query']} ({entry['results_count']} результатов) - {entry['timestamp']}")
    
    # Популярные запросы
    print("\n" + "-" * 60)
    response = requests.get(f"{API_BASE}/history/popular?limit=5")
    if response.status_code == 200:
        data = response.json()
        print("\nПопулярные запросы:")
        for item in data['popular']:
            print(f"  - {item['query']} ({item['count']} раз)")


# 5. Аналитика поиска
def search_analytics():
    """Пример получения аналитики"""
    print("\n" + "=" * 60)
    print("5. Аналитика поиска")
    print("=" * 60)
    
    response = requests.get(f"{API_BASE}/analytics/search?period=7d")
    if response.status_code == 200:
        data = response.json()
        print(f"\nПериод: {data['period']}")
        print(f"Всего поисков: {data['total_searches']}")
        print(f"Уникальных запросов: {data['unique_queries']}")
        
        if data['top_queries']:
            print("\nТоп запросов:")
            for item in data['top_queries'][:5]:
                print(f"  - {item['query']} ({item['count']} раз)")


# 6. Экспорт результатов
def export_results():
    """Пример экспорта результатов"""
    print("\n" + "=" * 60)
    print("6. Экспорт результатов")
    print("=" * 60)
    
    # JSON экспорт
    print("\nЭкспорт в JSON...")
    response = requests.get(f"{API_BASE}/search/export?q=6205&format=json")
    if response.status_code == 200:
        print(f"Получено {len(response.json())} результатов")
    
    # CSV экспорт
    print("\nЭкспорт в CSV...")
    response = requests.get(f"{API_BASE}/search/export?q=6205&format=csv")
    if response.status_code == 200:
        with open("results.csv", "wb") as f:
            f.write(response.content)
        print("Сохранено в results.csv")
    
    # XLSX экспорт
    print("\nЭкспорт в XLSX...")
    response = requests.get(f"{API_BASE}/search/export?q=6205&format=xlsx")
    if response.status_code == 200:
        with open("results.xlsx", "wb") as f:
            f.write(response.content)
        print("Сохранено в results.xlsx")


# 7. Экспорт аналогов
def export_analogs():
    """Пример экспорта аналогов"""
    print("\n" + "=" * 60)
    print("7. Экспорт аналогов")
    print("=" * 60)
    
    bearing_code = "6205"
    
    # JSON экспорт
    response = requests.get(f"{API_BASE}/analogs/{bearing_code}/export?format=json")
    if response.status_code == 200:
        data = response.json()
        print(f"\nАналоги для {bearing_code}:")
        for analog in data:
            print(f"  - {analog['code']} ({analog['manufacturer']})")
    
    # CSV экспорт
    response = requests.get(f"{API_BASE}/analogs/{bearing_code}/export?format=csv")
    if response.status_code == 200:
        with open(f"analogs_{bearing_code}.csv", "wb") as f:
            f.write(response.content)
        print(f"\nСохранено в analogs_{bearing_code}.csv")


# 8. Массовый экспорт
def batch_export():
    """Пример массового экспорта"""
    print("\n" + "=" * 60)
    print("8. Массовый экспорт")
    print("=" * 60)
    
    queries = ["6205", "6305", "6405"]
    
    response = requests.post(
        f"{API_BASE}/export/batch?format=xlsx",
        json=queries
    )
    
    if response.status_code == 200:
        with open("batch_export.xlsx", "wb") as f:
            f.write(response.content)
        print(f"Массовый экспорт выполнен для запросов: {', '.join(queries)}")
        print("Сохранено в batch_export.xlsx")


def main():
    """Запуск всех примеров"""
    print("Примеры использования API поиска")
    print("=" * 60)
    
    try:
        autocomplete_example()
        search_with_similar()
        get_similar_documents()
        search_history()
        search_analytics()
        export_results()
        export_analogs()
        batch_export()
        
        print("\n" + "=" * 60)
        print("Все примеры выполнены!")
        print("=" * 60)
    
    except requests.exceptions.ConnectionError:
        print("\n⚠️  Ошибка: API сервер не запущен")
        print("Запустите сервер командой: uvicorn api.app.api:app --reload")
    except Exception as e:
        print(f"\n⚠️  Ошибка: {e}")


if __name__ == '__main__':
    main()
