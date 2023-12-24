# EnSFile Encrypter

EnSFile Encrypter is a simple tool (v1.0.0 Unicode Scroll) for file encryption and decryption.

## Usage Options:

- `en`: Encrypt
- `de`: Decrypt

## How to Use with Command Line:

```
command <option> <filename> <customKey(Optional)>
```

## Example Using:

1. Encrypt a file without a custom key:
   ```
   command en text.txt
   ```

2. Decrypt a file without a custom key:
   ```
   command de text.txt
   ```

3. Encrypt a file with a custom key:
   ```
   command en text.txt 12345
   ```

4. Decrypt a file with a custom key:
   ```
   command de text.txt 12345
   ```
