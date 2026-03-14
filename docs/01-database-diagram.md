# Database Diagram --- Sistem E-commerce

Dokumentasi ini dibuat oleh: **Hanifa_Ramadhani**

Database yang digunakan pada sistem ini adalah **Sistem E-commerce**

## Entity Relationship Diagram

```mermaid
erDiagram
    CUSTOMERS ||--o{ ORDERS : places
    ORDERS ||--|{ ORDER_ITEMS : contains
    PRODUCTS ||--o{ ORDER_ITEMS : ordered_in
    CATEGORIES ||--o{ PRODUCTS : categorizes
    ORDERS ||--o| PAYMENTS : settled_by

    CUSTOMERS {
        int id PK
        varchar name
        varchar email
        varchar phone
        text shipping_address
        date register_date
    }

    CATEGORIES {
        int id PK
        varchar name
        text description
    }

    PRODUCTS {
        int id PK
        varchar name
        text description
        decimal price
        int stock_quantity
        int category_id FK
    }

    ORDERS {
        int id PK
        int customer_id FK
        datetime order_date
        decimal total_amount
        varchar status
    }

    ORDER_ITEMS {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }

    PAYMENTS {
        int id PK
        int order_id FK
        datetime payment_date
        varchar payment_method
        decimal amount
        varchar status
    }
```

## Penjelasan

### Customers

Menyimpan informasi pelanggan yang terdaftar, termasuk alamat pengiriman dan kontak.

### Categories

Menyimpan kategori produk (misalnya: Elektronik, Pakaian, Makanan) untuk memudahkan pengelompokan.

### Products

Menyimpan detail produk yang dijual, harga, serta jumlah stok yang tersedia di gudang.

### Orders

Menyimpan data transaksi utama yang dilakukan oleh pelanggan, termasuk tanggal transaksi dan status pesanan (misal: Pending, Shipped, Completed).

### Order Items

Menyimpan rincian produk apa saja yang dibeli dalam satu nomor pesanan (tabel ini menangani hubungan many-to-many antara Orders dan Products).

### Payments

Menyimpan informasi pembayaran untuk setiap pesanan, termasuk metode pembayaran (Transfer Bank, Kartu Kredit, E-Wallet) dan status pembayarannya.

---

_Dokumen ini dibuat sebagai bagian dari proyek Sistem E-Commerce oleh Hanifa Ramadhani_
