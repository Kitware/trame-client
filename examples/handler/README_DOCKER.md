# Using Handler with default Docker setup
This can work out of the box with the default docker bundle.  
All you have to do is updating the `setup/initialize.sh` script to run the app once so that asset collection can occur.  
Example: 
```bash
python -m your-trame-app-entrypoint --timeout 1 --server
```
