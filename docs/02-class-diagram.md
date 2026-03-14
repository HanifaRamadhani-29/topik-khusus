# Class Diagram --- Sistem E-commerce

Dokumentasi ini dibuat oleh: **Hanifa Ramadhani**

Class diagram menggambarkan struktur class dalam aplikasi **Sistem E-commerce**

```mermaid
classDiagram
    class Customer {
        - id: int
        - name: string
        - email: string
        - phone: string
        - shippingAddress: string
        - registerDate: date
        + placeOrder(): void
        + viewOrderHistory(): list
        + updateProfile(): void
    }

    class Category {
        - id: int
        - name: string
        - description: string
        + getProducts(): list
    }

    class Product {
        - id: int
        - name: string
        - description: string
        - price: double
        - stockQuantity: int
        + isStockAvailable(quantity: int): boolean
        + updateStock(quantity: int): void
        + getDetails(): string
    }

    class Order {
        - id: int
        - orderDate: datetime
        - totalAmount: double
        - status: string
        + calculateTotal(): void
        + updateStatus(newStatus: string): void
        + cancelOrder(): void
    }

    class OrderItem {
        - id: int
        - quantity: int
        - unitPrice: double
        + subTotal(): double
    }

    class Payment {
        - id: int
        - paymentDate: datetime
        - paymentMethod: string
        - amount: double
        - status: string
        + processPayment(): boolean
        + refund(): void
    }

    Customer "1" --> "many" Order : places
    Order "1" *-- "many" OrderItem : contains
    OrderItem "many" --> "1" Product : references
    Product "many" --> "1" Category : belongs_to
    Order "1" -- "0..1" Payment : settled_by
```

## Penjelasan

### Customer

Merepresentasikan pelanggan yang terdaftar di sistem. Memiliki kemampuan untuk melakukan pesanan, melihat riwayat belanja, dan mengelola profil pribadi.

### Category

Digunakan untuk mengelompokkan produk. Satu kategori dapat memiliki banyak produk (misalnya: Elektronik, Fashion, atau Peralatan Rumah Tangga).

### Product

Merepresentasikan barang yang dijual. Menyimpan informasi harga dan stok. Memiliki logika untuk mengecek apakah stok mencukupi sebelum pesanan diproses.

### Order

Merepresentasikan transaksi belanja. Kelas ini mengelola status pesanan (Pending, Dikirim, Selesai) dan menghitung total biaya dari seluruh item yang dibeli.

### Orderitem

Merupakan rincian produk dalam satu pesanan tertentu. Menyimpan jumlah (quantity) dan harga satuan pada saat transaksi terjadi (untuk menghindari masalah jika harga produk berubah di masa depan).

### Payment

Menangani informasi pembayaran pelanggan. Mencatat metode yang digunakan (seperti Transfer Bank atau E-Wallet) dan status keberhasilan transaksi pembayaran.

---

_Dokumen ini dibuat sebagai bagian dari proyek Sistem E-commerce oleh Hanifa Ramadhani_
