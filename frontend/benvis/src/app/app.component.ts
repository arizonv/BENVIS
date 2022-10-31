import { Component } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'benvis';
  personas!: any;


  constructor(private api: ApiService){

  }

  ngOnInit() {
    this.cargarData();
  }

  cargarData(){
    this.api.getPersonas().subscribe((data)=>{
      this.personas = data
      console.log(this.personas);
    });
  }
}
