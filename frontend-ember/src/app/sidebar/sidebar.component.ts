import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  // FOR FILE UPLOADER
  // files?: any = [];

  // uploadFile(event: any) {
  //   for (let index = 0; index < event.length; index++) {
  //     const element = event[index];
  //     this.files.push(element.name)
  //   }
  // }
  // deleteAttachment(index: any) {
  //   this.files.splice(index, 1)
  // }

  constructor() { }

  ngOnInit(): void {
  }

}

