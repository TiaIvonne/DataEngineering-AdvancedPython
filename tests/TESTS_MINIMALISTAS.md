# Tests Minimalistas - Checklist

## Tests para Cache

### Tests Completados ✅
- [x] Test 1: Inicialización básica
- [x] Test 3: Directorio por defecto
- [x] Tests 4-6: Propiedades (app_name, cache_dir, obsolescence)
- [x] Test indirecto: __get_file_path (a través de set())

### Tests Pendientes
- [ ] **Test 7**: `set()` crea archivo → `exists()` retorna True
- [ ] **Test 11**: `exists()` retorna False para archivo inexistente
- [ ] **Test 13**: `load()` carga contenido correcto
- [ ] **Test 14**: `load()` lanza CacheError si no existe
- [ ] **Test 20**: `delete()` elimina archivo

---

## Tests para CacheURL

### Tests Pendientes
- [ ] **Test 1**: Inicialización de CacheURL
- [ ] **Test 2**: `get()` descarga y guarda (con mock)
- [ ] **Test 3**: `get()` usa caché si existe

---

## Tests para MadridFines

### Tests Pendientes
- [ ] **Test 1**: Inicialización de MadridFines
- [ ] **Test 2**: `add()` carga un mes (con mocks)
- [ ] **Test 3**: (Opcional) Un método público básico

---

## Código de Referencia Rápida

### Cache - Test 7: set() crea archivo
```python
def test_set_creates_file(cache_instance):
    """Test 7: Verificar que set() crea archivo"""
    cache_instance.set("test.txt", "contenido")
    assert cache_instance.exists("test.txt")
    assert cache_instance.load("test.txt") == "contenido"
```

### Cache - Test 11: exists() retorna False
```python
def test_exists_returns_false(cache_instance):
    """Test 11: Verificar que exists() retorna False"""
    assert not cache_instance.exists("inexistente.txt")
```

### Cache - Test 13: load() carga archivo
```python
def test_load_existing_file(cache_instance):
    """Test 13: Verificar que load() carga archivo"""
    cache_instance.set("test.txt", "contenido")
    assert cache_instance.load("test.txt") == "contenido"
```

### Cache - Test 14: load() lanza error
```python
def test_load_nonexistent_raises_error(cache_instance):
    """Test 14: Verificar que load() lanza CacheError"""
    with pytest.raises(CacheError):
        cache_instance.load("inexistente.txt")
```

### Cache - Test 20: delete() elimina archivo
```python
def test_delete_file(cache_instance):
    """Test 20: Verificar que delete() elimina archivo"""
    cache_instance.set("test.txt", "contenido")
    cache_instance.delete("test.txt")
    assert not cache_instance.exists("test.txt")
```

### CacheURL - Test 1: Inicialización
```python
def test_cacheurl_init(temp_cache_dir):
    """Test: Verificar inicialización de CacheURL"""
    from traficFines.cacheURL import CacheURL
    cache_url = CacheURL("TestApp", obsolescence=7, cache_dir=temp_cache_dir)
    assert cache_url.app_name == "TestApp"
```

### CacheURL - Test 2: get() descarga y guarda
```python
def test_cacheurl_get_downloads_and_saves(mock_requests_get, cacheurl_instance):
    """Test: Verificar que get() descarga y guarda"""
    from unittest.mock import Mock
    # Mock de respuesta HTTP
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "contenido descargado"
    mock_requests_get.return_value = mock_response
    
    url = "https://example.com/test.txt"
    contenido = cacheurl_instance.get(url)
    
    assert contenido == "contenido descargado"
    assert cacheurl_instance.exists(url)
```

### CacheURL - Test 3: get() usa caché
```python
def test_cacheurl_get_uses_cache(cacheurl_instance):
    """Test: Verificar que get() usa caché si existe"""
    url = "https://example.com/test.txt"
    url_hash = cacheurl_instance._CacheURL__url_to_hash(url)
    cacheurl_instance.set(url_hash, "cached")
    
    contenido = cacheurl_instance.get(url)
    assert contenido == "cached"
```

### MadridFines - Test 1: Inicialización
```python
def test_madridfines_init():
    """Test: Verificar inicialización de MadridFines"""
    from traficFines.madridFines import MadridFines
    madrid = MadridFines("TestApp", obsolescence=7)
    assert madrid._MadridFines__data.empty
    assert madrid._MadridFines__loaded == []
```

### MadridFines - Test 2: add() carga un mes
```python
def test_madridfines_add_month(mock_requests_get, mock_beautifulsoup, madridfines_instance):
    """Test: Verificar que add() carga un mes"""
    # Requiere mocks complejos - implementar después
    pass
```

---

## Notas Importantes

### Para CacheURL:
- Necesitas agregar fixture `cacheurl_instance` en `conftest.py`
- Necesitas agregar fixture `mock_requests_get` en `conftest.py`

### Para MadridFines:
- Necesitas agregar fixture `madridfines_instance` en `conftest.py`
- Necesitas mocks para `requests.get` y `BeautifulSoup`
- Los tests de MadridFines son más complejos, dejarlos para el final

### Prioridad de Implementación:
1. ✅ Cache - Tests básicos (ya completados)
2. ⏳ Cache - Tests de métodos esenciales (5 tests)
3. ⏳ CacheURL - Tests básicos (3 tests)
4. ⏳ MadridFines - Tests básicos (2-3 tests)

---

## Estado Actual
- **Cache**: 6/11 tests completados
- **CacheURL**: 0/3 tests completados
- **MadridFines**: 0/2 tests completados

**Total**: 6/16 tests completados

