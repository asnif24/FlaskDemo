```
# 初始化資料庫  
flask db init -d apps/migrations  
# 產生資料庫遷移檔案  
flask db migrate -d apps/migrations

---  

# 將遷移資料實際套用至資料庫
flask db upgrade -d apps/migrations  
# 將已遷移資料還原成先前的狀態
flask db downgrade -d apps/migrations  
```