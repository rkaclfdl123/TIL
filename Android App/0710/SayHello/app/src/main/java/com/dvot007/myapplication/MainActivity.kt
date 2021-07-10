package com.dvot007.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.dvot007.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    val binding by lazy { ActivityMainBinding.inflate(layoutInflater) }
    //바인딩 변수에 지연초기화를 사용해서 특정 ~를 담을거야


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.btnSay.setOnClickListener {
        binding.textView.text="text Kotlin!"
        //버튼에 접근 binging으로 해야
            }
    }
}