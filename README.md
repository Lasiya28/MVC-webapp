### MVC Design Pattern Implementation:

*   **Models**: SQLAlchemy models in models/ directory define database tables
    
*   **Views**: Represented by Pydantic schemas in schemas/ directory for validation and serialization
    
*   **Controllers**: API endpoints in controllers/ directory handle HTTP requests
    
*   **Services**: Business logic in services/ directory
    

### Key Features:

1.  **Authentication Endpoints**
    
    *   /signup: Creates a new user and returns a JWT token
        
    *   /login: Authenticates a user and returns a JWT token
        
2.  **Post Management Endpoints**
    
    *   /posts (POST): Creates a new post
        
    *   /posts (GET): Retrieves all posts for the authenticated user
        
    *   /posts/{post\_id} (DELETE): Deletes a specific post
        
3.  **Security Features**
    
    *   Password hashing with bcrypt
        
    *   JWT token-based authentication
        
    *   Dependency injection for protected routes
        
4.  **Data Validation**
    
    *   Pydantic models with extensive validation for all input data
        
    *   Request body size validation for the AddPost endpoint (1MB limit)
        
5.  **Caching**
    
    *   In-memory caching for GetPosts endpoint with 5-minute TTL
        
6.  **Database Integration**
    
    *   SQLAlchemy ORM models with appropriate relationships
        
    *   MySQL database connection
