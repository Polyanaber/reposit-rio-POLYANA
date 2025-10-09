// service-worker.js - Versão Simplificada e Funcional
const CACHE_NAME = 'smartmind-v1.0.0';
const STATIC_FILES = [
  '/',
  '/index.html',
  './',
  './index.html'
];

// Instalação
self.addEventListener('install', (event) => {
  console.log('🛠️ Service Worker instalando...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('📦 Cache aberto, adicionando arquivos...');
        return cache.addAll(STATIC_FILES);
      })
      .then(() => {
        console.log('✅ Service Worker instalado');
        return self.skipWaiting();
      })
      .catch((error) => {
        console.error('❌ Erro na instalação:', error);
      })
  );
});

// Ativação
self.addEventListener('activate', (event) => {
  console.log('🚀 Service Worker ativando...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('🗑️ Removendo cache antigo:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      console.log('✅ Service Worker ativado');
      return self.clients.claim();
    })
  );
});

// Fetch - Estratégia Cache First
self.addEventListener('fetch', (event) => {
  // Ignora requisições não-GET
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        // Retorna do cache se disponível
        if (cachedResponse) {
          return cachedResponse;
        }

        // Busca na rede
        return fetch(event.request)
          .then((networkResponse) => {
            // Verifica se a resposta é válida
            if (!networkResponse || networkResponse.status !== 200) {
              return networkResponse;
            }

            // Adiciona ao cache
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseClone);
              });

            return networkResponse;
          })
          .catch((error) => {
            console.log('🌐 Offline - recurso não disponível:', event.request.url);
            
            // Para páginas HTML, retorna a página principal do cache
            if (event.request.destination === 'document') {
              return caches.match('/');
            }
            
            // Para outros recursos, retorna resposta vazia
            return new Response('', {
              status: 408,
              statusText: 'Offline'
            });
          });
      })
  );
});

// Mensagens do App
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

console.log('📡 Service Worker do SmartMind carregado!');
