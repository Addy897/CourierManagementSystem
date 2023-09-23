import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView,convert_coordinates_to_address,convert_address_to_coordinates


class MapBox:
    def __init__(this,window=None):
        this.window1=window
        this.root=tkinter.Toplevel()
        this.root.title("Select Address")
        this.root.geometry(f"800x750")

        
        this.root.bind("<Return>", this.search)

        this.search_bar = tkinter.Entry(this.root, width=50)
        this.search_bar.grid(row=0, column=0, pady=10, padx=10, sticky="we")
        this.search_bar.focus()

        this.search_bar_button = tkinter.Button(master=this.root, width=8, text="Search", command=this.search)
        this.search_bar_button.grid(row=0, column=1, pady=10, padx=10)


        this.map_widget = TkinterMapView(master=this.root,width=800, height=600, corner_radius=0)
        this.map_widget.grid(row=1, column=0, columnspan=3, sticky="nsew")
        this.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
        this.map_widget.add_right_click_menu_command(label="Set Location",\
                                        command=this.placeMarker,\
                                        pass_coords=True)
        this.map_widget.set_address("india")

        this.search_marker = None
        this.search_in_progress = False
        this.count=0
        this.addr=""
        #this.root.destroy()
    
        
    def placeMarker(this,cord):
        try:
            address=convert_coordinates_to_address(cord[0],cord[1])
            if(address.country != "India"):
                tkinter.messagebox.showerror("error","Select Only India",)
                this.map_widget.set_address("India")
                return

            if(this.search_marker is not None):
                this.search_marker.delete()
            this.search_marker = this.map_widget.set_marker(cord[0],cord[1],text=address.address)
            this.search_bar.delete(0,tkinter.END)
            this.search_bar.insert(0,address.address)
            this.addr=address
            #print(this.addr)
            
        except Exception as e:
            print("[-] Error In MapBox placeMarker:",e)
    def search(this, event=None):
        
        if not this.search_in_progress:
            this.search_in_progress = True
            address = this.search_bar.get()
            cord=convert_address_to_coordinates(address)
            this.map_widget.set_address(address)
            if(this.search_marker is not None):
                this.search_marker.delete()
            this.search_marker = this.map_widget.set_marker(cord[0],cord[1],text=address)
            if this.search_marker is False:
               # print(address)
                this.search_marker = None
            this.search_in_progress = False
            this.addr=address


        
           

    

    def on_closing(this, event=0):
        this.root.destroy()
           
        


    def start(this):
        this.window1.wait_window(this.root)
        return this.addr
if __name__ =="__main__":
    m=MapBox()
    print(m.start())

