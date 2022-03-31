import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

export class Student {
  constructor(
    public fullname: string,
    public email: string,
    public phone: number,
  ) {
  }
}
@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit {

  students : Student[];

  constructor(
    private httpClient: HttpClient
  ) { }

  ngOnInit(): void {
    this.getStudents();
  }

  getStudents(){
    this.httpClient.get<any>('https://reqres.in/api/products').subscribe(
      response => {
        console.log(response);
      }
    );
  }

}
