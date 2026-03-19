# Using PreProcessor with default Docker setup
This can work out of the box with the default docker bundle.  
All you have to do is updating the `setup/initialize.sh` script to run the app once so that asset collection can occur.  
Example: 
```bash
uv run your-trame-app-entrypoint --timeout 1
```
