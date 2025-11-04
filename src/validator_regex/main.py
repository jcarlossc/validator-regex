from validator_regex.RegexValidator import RegexValidator

def main() -> None:

    print(RegexValidator.is_email("teste@dominio.com")) 
    print(RegexValidator.is_email("testedominio.com")) 
    print(RegexValidator.is_brl("R$ 44,44")) 
    print(RegexValidator.is_brl("R$ 44.44")) 
    print(RegexValidator.is_cpf("123.456.789-09"))     
    print(RegexValidator.is_cpf("123.456.789-0"))     
    print(RegexValidator.is_cnpj("12.123.123/4564-44"))     
    print(RegexValidator.is_cnpj("12.123.123/4564-4"))     
    print(RegexValidator.is_time("23:59"))     
    print(RegexValidator.is_time("23:5"))     
    print(RegexValidator.is_name("Carlos"))     
    print(RegexValidator.is_name("Carlos123"))     




if __name__ == "__main__":
    main()