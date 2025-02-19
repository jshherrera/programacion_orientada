def test():
    name = "Juan"  # nombre de prueba
    check_output = nombre()
    expected_output = f"Hola {name}"
    if check_output == expected_output:
        print("Test es OK")
    else:
        print(f'Test no es OK! Se esperaba "{expected_output}"')
        print(f'Pero se recibió "{check_output}"')

if __name__ == "__main__":
    test()