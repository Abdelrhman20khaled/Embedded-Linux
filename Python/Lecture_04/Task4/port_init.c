void GPIO_Init(void)
{
    // Define all Register at firt as output pins
    DDRA = 0x1f;
    DDRB = 0xFF;
    DDRC = 0xFF;
    DDRD = 0xFF;
}        
    