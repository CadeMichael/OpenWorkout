import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' show jsonDecode;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String newWeight = '';

  void getWeight() async {
    var url = Uri.parse(
        'http://localhost:8000/ri/{reps, desired_ri, one_rm}?reps=10&desired_ri=100&one_rm=300');

    var response = await http.get(url);
    var weight = jsonDecode(response.body);
    setState(() {
      newWeight = weight.toString();
    });
  }
  void getWeightGo() async {
    var go = 'http://localhost:8080/max?weight=10&reps=15';
    var url = Uri.parse(go);

    var response = await http.get(url);
    var weight = (response.body);
    setState(() {
      newWeight = weight;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('is the new weight there? ${newWeight}'),
            FloatingActionButton(
              onPressed: () {
                getWeight();
              },
            ),
          ],
        ),
      ),
    );
  }
}
