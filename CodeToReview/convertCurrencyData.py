from CurrencyScannerNBP import CurrencyScanner
import logging as log

# Configure the logger
log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %h:%M:%S')

def main(output_format: str='xml'):
    """Fetch currency 
    from the API and save them to files in the specified format.

    Parameters:
    - output_format: the format of the output files. Can be 'json' or 'xml'. Defaults to 'xml'.

    Returns:
    - None
    """
    headers = dict(
        Accept = f'Applications/{output_format}'
    )
    #duplicated code - I can see that first two rows of both output formats are the same
    if output_format == 'json':
        curr_scanner = CurrencyScanner(output_format)
        rates = curr_scanner.get_currency_rates(headers)
        data = curr_scanner.combine_to_json(rates)
    if output_format == 'xml':
        curr_scanner = CurrencyScanner(output_format)
        rates = curr_scanner.get_currency_rates(headers)
        data = curr_scanner.jsonToXml(curr_scanner.combine_to_json(rates))
    
    #probably it would be easier to extend if possible output fromats was enum. then you can easli add new format and override function 'saveToFile' 
    #and finally add the empty class which will be defualt (if str given by user is not in enum, then enum will have defualt value (for example NoneFormat, which
    #will raise an error during function saveTofile - then you dont need to have additional checking if the given format is one of acceptable
    if output_format != 'xml' and output_format != 'json':
        raise ValueError("Unsupported output format: {}".format(output_format))

    file_name = f'rates_{rates[0]["effectiveDate"]}'
    curr_scanner.watermark(data, file_name=file_name, file_format=output_format)


if __name__ == '__main__':
    #testing in main - great job xd
    log.info("Testing xlm file format")
    main()
    log.info("Testing json file format")
    main("json")
