# SDLC Process --- Sistem Ecommerce

Dokumentasi ini dibuat oleh: **Hanifa Ramadhani**

Dokumentasi ini menjelaskan proses SDLC (Software Development Life Cycle) untuk pengembangan aplikasi Sistem e-commerce.

## Tahapan SDLC

```mermaid
stateDiagram-v2
    [*] --> Planning: Permintaan\nPengembangan

    state Planning {
        [*] --> Requirements
        Requirements --> Analysis: Kebutuhan\nJelas
        Analysis --> Design: Specifikasi\nSelesai
        Design --> [*]
    }

    state Implementation {
        [*] --> Coding
        Coding --> Testing: Kode\nSelesai
        Testing --> [*]
    }

    state Deployment {
        [*] --> Staging
        Staging --> Production: UAT\nLulus
        Production --> Maintenance: Sistem\nAktif
        Maintenance --> [*]
    }

    Planning --> Implementation
    Implementation --> Deployment
    Deployment --> Planning: Update/\nEnhancement
```

## Detail Tahapan

### 1. Planning (Perencanaan)

```mermaid
flowchart LR
    subgraph Planning
        RG[Requirements Gathering]
        FS[Feasibility Study]
        PP[Project Plan]
    end

    RG --> FS
    FS --> PP
```

**Aktivitas:**

- Mengumpulkan kebutuhan bisnis
- Analisis kelayakan proyek
- Membuat rencana proyek dan timeline

### 2. Analysis (Analisis)

```mermaid
flowchart LR
    subgraph Analysis
        UCA[Use Case Analysis]
        SM[System Modeling]
        RS[Requirements\nSpecification]
    end

    UCA --> SM
    SM --> RS
```

**Aktivitas:**

- Analisis kebutuhan fungsional dan non-fungsional
- Membuat use case diagram
- Membuat spesifikasi sistem

### 3. Design (Desain)

```mermaid
flowchart LR
    subgraph Design
        DD[Database Design]
        AD[Architecture Design]
        ID[Interface Design]
    end

    DD --> AD
    AD --> ID
```

**Aktivitas:**

- Desain database (Entity Relationship Diagram)
- Desain arsitektur aplikasi
- Desain antarmuka pengguna

### 4. Implementation (Implementasi)

```mermaid
flowchart LR
    subgraph Implementation
        DS[Database Setup]
        BD[Backend Development]
        FD[Frontend Development]
        INT[Integration]
    end

    DS --> BD
    BD --> FD
    FD --> INT
```

**Aktivitas:**

- Setup database MySQL
- Pengembangan backend API
- Pengembangan frontend
- Integrasi sistem

### 5. Testing (Pengujian)

```mermaid
flowchart LR
    subgraph Testing
        UT[Unit Testing]
        IT[Integration Testing]
        ST[System Testing]
        UAT[User Acceptance\nTesting]
    end

    UT --> IT
    IT --> ST
    ST --> UAT
```

**Aktivitas:**

- Unit testing setiap komponen
- Integration testing antar modul
- System testing keseluruhan sistem
- User Acceptance Testing (UAT)

### 6. Deployment (Penempatan)

```mermaid
flowchart LR
    subgraph Deployment
        SD[Staging\nDeployment]
        PD[Production\nDeployment]
        CFG[Configuration]
    end

    SD --> PD
    PD --> CFG
```

**Aktivitas:**

- Deploy ke environment staging
- Konfigurasi production
- Deploy ke production server

### 7. Maintenance (Pemeliharaan)

```mermaid
flowchart LR
    subgraph Maintenance
        BF[Bug Fixing]
        PM[Performance\nMonitoring]
        SU[System Update]
        BR[Backup & Recovery]
    end

    BF --> PM
    PM --> SU
    SU --> BR
```

**Aktivitas:**

- Perbaikan bug
- Monitoring performa sistem
- Update sistem
- Backup dan recovery data

## Tim Pengembangan

```mermaid
classDiagram
    class ProjectManager {
        - Coordinating
        - Planning
    }

    class SystemAnalyst {
        - Requirements
        - Analysis
    }

    class DatabaseAdmin {
        - Database Design
        - Data Management
    }

    class BackendDeveloper {
        - API Development
        - Business Logic
    }

    class FrontendDeveloper {
        - UI Development
        - User Experience
    }

    class QAEngineer {
        - Testing
        - Quality Assurance
    }

    ProjectManager --> SystemAnalyst
    SystemAnalyst --> DatabaseAdmin
    SystemAnalyst --> BackendDeveloper
    SystemAnalyst --> FrontendDeveloper
    BackendDeveloper --> QAEngineer
    FrontendDeveloper --> QAEngineer
```

## Timeline Pengembangan

```mermaid
gantt
    title Timeline Pengembangan Sistem Perpustakaan
    dateFormat  YYYY-MM-DD

    section Planning
    Requirements Gathering   :a1, 2026-03-06, 7d
    Feasibility Study        :a2, after a1, 3d
    Project Plan             :a3, after a2, 2d

    section Analysis
    Use Case Analysis        :b1, after a3, 5d
    System Modeling          :b2, after b1, 5d

    section Design
    Database Design          :c1, after b2, 5d
    Architecture Design      :c2, after c1, 5d
    Interface Design         :c3, after c2, 5d

    section Implementation
    Database Setup           :d1, after c3, 3d
    Backend Development      :d2, after d1, 15d
    Frontend Development     :d3, after d2, 15d
    Integration              :d4, after d3, 5d

    section Testing
    Unit Testing             :e1, after d4, 5d
    Integration Testing      :e2, after e1, 5d
    System Testing           :e3, after e2, 5d
    UAT                      :e4, after e3, 5d

    section Deployment
    Staging Deployment       :f1, after e4, 3d
    Production Deployment    :f2, after f1, 2d
```

## Deliverables

| Tahapan        | Deliverables                                                |
| -------------- | ----------------------------------------------------------- |
| Planning       | Project Charter, Requirements Document                      |
| Analysis       | Use Case Diagram, SRS (Software Requirements Specification) |
| Design         | ERD, Class Diagram, Architecture Document                   |
| Implementation | Source Code, Database Schema, API Documentation             |
| Testing        | Test Cases, Test Reports, Bug Reports                       |
| Deployment     | Deployment Guide, Configuration Guide                       |
| Maintenance    | System Documentation, User Manual                           |

---

_Dokumen ini dibuat sebagai bagian dari proyek Sistem Ecommerce oleh Hanifa Ramadhani_
