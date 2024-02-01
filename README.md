# Waterdip AI Assignment

This is a simple FastAPI project for managing tasks.

## Endpoints

1. **Get All Tasks**
   - Method: `GET`
   - Endpoint: `/v1/tasks`
   - Description: Retrieve a list of all tasks.

2. **Get Task by ID**
   - Method: `GET`
   - Endpoint: `/v1/tasks/{task_id}`
   - Description: Retrieve details of a specific task by its ID.

3. **Create Task**
   - Method: `POST`
   - Endpoint: `/v1/tasks`
   - Description: Create a new task.
   - Input:
     ```json
     { "title": "Task Title", "is_completed": false }
     ```
   - Output:
     ```json
     { "id": 1 }
     ```

4. **Bulk Create Tasks**
   - Method: `POST`
   - Endpoint: `/v1/tasks/bulk`
   - Description: Bulk create tasks.
   - Input:
     ```json
     {
       "tasks": [
         { "title": "Task 1", "is_completed": false },
         { "title": "Task 2", "is_completed": true }
       ]
     }
     ```
   - Output:
     ```json
     {
       "tasks": [
         { "id": 1 },
         { "id": 2 }
       ]
     }
     ```

5. **Delete Task**
   - Method: `DELETE`
   - Endpoint: `/v1/tasks/{task_id}`
   - Description: Delete a specific task by ID.

6. **Bulk Delete Tasks**
   - Method: `DELETE`
   - Endpoint: `/v1/tasks/bulk`
   - Description: Bulk delete tasks.
   - Input:
     ```json
     {
       "tasks": [
         { "id": 1 },
         { "id": 2 }
       ]
     }
     ```

7. **Update Task**
   - Method: `PUT`
   - Endpoint: `/v1/tasks/{task_id}`
   - Description: Update the title or completion status of a specific task.
   - Input:
     ```json
     { "title": "New Title", "is_completed": true }
     ```
   - Output: `204 No Content`

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
