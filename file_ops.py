cat > python_code/file_ops.py <<'EOF'
# Файлға жазу
with open("example.txt", "w") as f:
    f.write("Hello from Python!\n")

# Файлдан оқу
with open("example.txt", "r") as f:
    content = f.read()

print("Файлдан оқылды:", content)
EOF
