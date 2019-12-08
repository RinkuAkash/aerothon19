import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit{
  user:any=null;
  constructor(public auth: AuthService) {}
  ngOnInit(){
    this.auth.login();
    this.user=this.auth.user;
  }
}
