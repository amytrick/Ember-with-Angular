import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';


@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {
  content: any;
  constructor(private modalService: NgbModal) { }

  ngOnInit(): void {
  }

  open(content: any) {
    this.modalService.open(content);
  }

}
