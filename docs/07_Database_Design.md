\## Projects



| Field | Type | Constraints | Description |

|--------|------|-------------|-------------|

| id | UUID | Primary Key | Unique project identifier |

| title | VARCHAR(150) | NOT NULL | Project title |

| description | TEXT | NOT NULL | Project description |

| created\_by | UUID | FK → Users(id) | Project creator (Client) |

| total\_amount | DECIMAL(12,2) | NOT NULL | Total agreed project value |

| currency | CHAR(3) | DEFAULT 'INR' | Currency code |

| status | ENUM | NOT NULL | Current project status |

| start\_date | DATE | NULL | Starts after escrow funding |

| end\_date | DATE | NOT NULL | Agreed completion date |

| created\_at | TIMESTAMP | NOT NULL | Creation timestamp |

| updated\_at | TIMESTAMP | NOT NULL | Last updated |



\### Status Enum



\- DRAFT

\- INVITED

\- AWAITING\_ACCEPTANCE

\- PLANNING

\- AWAITING\_ESCROW

\- ACTIVE

\- ON\_HOLD

\- UNDER\_DISPUTE

\- COMPLETED

\- CANCELLED



\### Business Rules



\- Only clients can create projects.

\- Sellers must accept invitations before work begins.

\- Milestones must be finalized before escrow funding.

\- The sum of milestone amounts must equal the project's total amount.

\- A project becomes ACTIVE only after full escrow funding.

\- Project title, description, and total amount become immutable once the seller accepts.

\- Milestones and end date can only be modified through mutual agreement.

