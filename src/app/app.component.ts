import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'thegoldtree-rs';
  RSrequest;
  rsTitle = 'Um método para deduplicação de metadados bibliográficos baseado no empilhamento de classificadores';  ;
  rsAbstract;
  

  OnSubmit() {
    console.log("test");
    this.http.post('http://127.0.0.1:5000/rs', { titleabstract : this.rsTitle + this.rsAbstract }).subscribe(data => {
      this.RSrequest = data;
    })
    console.log(this.RSrequest);
  }

  constructor(private http: HttpClient) { }

  ngOnInit() {     

  }
}
