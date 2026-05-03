'use client'
import { useEffect, useState } from 'react'

interface InventoryItem {
  id: number;
  name: string;
  description: string;
  price: number;
  quantity: number;
}

export default function Home() {
  const [items, setItems] = useState<InventoryItem[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // ฟังก์ชันดึงข้อมูลจาก FastAPI Backend
    fetch('http://localhost:8000/items/')
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then((data) => {
        setItems(data)
        setLoading(false)
      })
      .catch((err) => {
        console.error('Fetch error:', err)
        setLoading(false)
      })
  }, [])

  return (
    <div style={{ 
      padding: '40px', 
      fontFamily: 'system-ui, -apple-system, sans-serif',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <header style={{ marginBottom: '30px', borderBottom: '2px solid #eee', paddingBottom: '10px' }}>
        <h1 style={{ fontSize: '2.5rem', color: '#1a1a1a', margin: 0 }}>
          📦 Inventory System
        </h1>
        <p style={{ color: '#666' }}>Software Deployment and Maintenance Project</p>
      </header>

      <main>
        {loading ? (
          <p>Loading items...</p>
        ) : items.length === 0 ? (
          <div style={{ 
            padding: '20px', 
            backgroundColor: '#f9f9f9', 
            borderRadius: '8px', 
            textAlign: 'center' 
          }}>
            <p>No items found in stock.</p>
            <small>Try adding items via Backend API (Postman or Swagger)</small>
          </div>
        ) : (
          <div style={{ display: 'grid', gap: '15px' }}>
            {items.map((item) => (
              <div key={item.id} style={{
                padding: '15px',
                border: '1px solid #ddd',
                borderRadius: '8px',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
              }}>
                <div>
                  <h3 style={{ margin: '0 0 5px 0' }}>{item.name}</h3>
                  <p style={{ margin: 0, fontSize: '0.9rem', color: '#555' }}>{item.description}</p>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontWeight: 'bold', fontSize: '1.1rem' }}>${item.price}</div>
                  <div style={{ 
                    fontSize: '0.8rem', 
                    color: item.quantity > 0 ? 'green' : 'red',
                    fontWeight: '500'
                  }}>
                    Stock: {item.quantity}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer style={{ marginTop: '50px', fontSize: '0.8rem', color: '#aaa', textAlign: 'center' }}>
        Built with Next.js + FastAPI + Docker
      </footer>
    </div>
  )
}
