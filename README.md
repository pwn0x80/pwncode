# pwncode
### shellcoding 

### Commands
- **Assembly Mode** - Press Enter two times (darkside mode)
- - press c, exit or done after entering assembly code
```
 pwncode 
pwncode#
type in Enter
---Darkside---
>mov eax,3
>mov eax, 3
>c
00000000  B803000000        mov eax,0x3
00000005  B803000000        mov eax,0x3
```

- **bits** - To change or check bits {16,32,64}
- -  (default= 64 bit)

```
pwncode# bits
Current bit 64
pwncode# bits 16
pwncode# bits
Current bit 16
pwncode#

```

# Installation

` git clone https://github.com/aditya0x80/pwncode.git `

to set access pwncode from any directory

` cp pwncode /usr/local/bin/ `

### Usage -

`pwncode`

or

`./pwncode`


### demo

![image](https://user-images.githubusercontent.com/25504458/125067038-57c13a80-e0d1-11eb-806d-9a3c70710b00.png)


![image](https://user-images.githubusercontent.com/25504458/124901325-866ee080-dfff-11eb-97f9-ef52dc793da0.png)
