"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal

# Core app schemas

class Employee(BaseModel):
    """
    Employees collection schema
    Collection name: "employee"
    """
    name: str = Field(..., description="Full name")
    role: Literal["Chef", "Waiter", "Manager", "Cashier", "Cleaner", "Host", "Delivery", "Other"] = Field(
        ..., description="Employee role"
    )
    phone: Optional[str] = Field(None, description="Phone number")
    email: Optional[str] = Field(None, description="Email address")
    hourly_rate: Optional[float] = Field(None, ge=0, description="Hourly pay rate")
    active: bool = Field(True, description="Employment status")


class MenuItem(BaseModel):
    """
    Menu items collection schema
    Collection name: "menuitem"
    """
    name: str = Field(..., description="Item name")
    description: Optional[str] = Field(None, description="Item description")
    category: Literal[
        "Starters", "Mains", "Desserts", "Beverages", "Sides", "Specials"
    ] = Field(..., description="Menu category")
    price: float = Field(..., ge=0, description="Price")
    available: bool = Field(True, description="Available for order")


# Example schemas (kept for reference)
class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")


class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Note: The Flames database viewer can read these via an endpoint.
